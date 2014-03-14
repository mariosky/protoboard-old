#!/usr/bin/env python

from activitytree.models import LearningActivity, UserProfile, LearningStyleInventory, ActivityTree, \
    UserLearningActivity
import datetime
from lxml import etree
#Exceptions




TRANSFORM = """<?xml version="1.0" encoding="utf-8"?>
<!--
	Author: Mario Garcia
	File:
	Date:
	Purpose: Crear elementos de navegacion a partir de XML
-->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:output method="html" indent="yes" encoding="utf-8" />

	<xsl:template match="/">
	<div id="navcontainer">
	    <ul id="navlist">
			<xsl:apply-templates select="item"/>
		</ul>
	</div>
	</xsl:template>


	<xsl:template match="item" >
      	<xsl:choose>

			<!-- CONTAINER-->
			<xsl:when test="@is_container = 'True'">
	            <li>
	             <xsl:attribute name="class">
	                    <xsl:if test="@is_visible = 'False'">hidden </xsl:if>
	                    <xsl:if test="@pre_condition = 'disabled'"> disabled </xsl:if>
						<xsl:value-of select="concat('container_', @objective_status)" />
	             </xsl:attribute>

	        		<a href="{@uri}">
						<xsl:value-of select="@identifier" />
	       		 	</a>
			    </li>
			  </xsl:when>

            <!-- ACTIVITY DISABLED -->
			<xsl:when test="@pre_condition = 'disabled'">
	            <li>
		             <xsl:attribute name="class">
			      		<xsl:if test="@pre_condition = 'disabled'">activity_disabled </xsl:if>
						<xsl:if test="@is_visible = 'False'">hidden </xsl:if>
			         </xsl:attribute>

	        		 <a href="#top">
					   <xsl:value-of select="@identifier"/> (<xsl:value-of select="@objective_measure"/>)
					 </a>
			    </li>
			</xsl:when>
			<xsl:when test="@is_current = 'True'">
	            <li class="activity_current">
	        		<a href="{@uri}">
						<xsl:value-of select="@identifier" />
	       		 	</a>
			    </li>
			</xsl:when>



          <xsl:when test="@objective_status = 'satisfied'">
            <li class="activity_satisfied">
        		<a href="{@uri}">
					<xsl:value-of select="@identifier"/> (<xsl:value-of select="@objective_measure"/>)
       		 	</a>
		    </li>
		  </xsl:when>

		   <xsl:when test="@objective_status = 'notSatisfied'">
            <li class="activity_notSatisfied">
        		<a href="{@uri}">
					<xsl:value-of select="@identifier"/>
       	            <xsl:if test="@recomended_value != 'None'">
        	             [<xsl:value-of select="@recomended_value"/>]
		            </xsl:if>
       		    </a>
		   </li>
		  </xsl:when>



            <xsl:otherwise>
            <li class="{@identifier}"/>

          </xsl:otherwise>
        </xsl:choose>


        <xsl:if test="item">

    		<ul>
				<xsl:apply-templates select="item"/>
			</ul>
		</xsl:if>
	</xsl:template>

</xsl:stylesheet>
"""


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message


class NotAllowed(Error):
    """Raised when an invalid action is encounterd

    Attributes:
        action  -- action to be executed
        message -- explanation of why the specific action is not allowed
    """

    def __init__(self, action, message):
        self.action = action
        self.message = message

    def __str__(self):
        return """%s not allowed, %s""" % (self.action, self.message,)


class SimpleSequencing(object):
    def set_current(self, ula):
        #if ula.learning_activity.root is None:
        #    raise NotAllowed('Set Current', "The root container cannot be the current activity")
        #if ula.learning_activity.is_container:
        #    raise NotAllowed('Set Current', "A container cannot be the current activity")

        if ula.learning_activity.root is not None:
            atree = ActivityTree.objects.get(user=ula.user, root_activity=ula.learning_activity.root)
        else:
            atree = ActivityTree.objects.get(user=ula.user, root_activity=ula.learning_activity)

        # Is there a current activity?
        # If its the same don't do anything
        # If is different raise error
        if atree.current_activity:
            if atree.current_activity == ula:
                return
            else:
                raise NotAllowed('Set Current', "Another activity is already the current activity")

        # Set current activity if everything is fine 
        atree.current_activity = ula
        ula.is_current = True
        ula.save()
        atree.save()

    def get_current(self, ula):
        if ula.learning_activity.root is not None:
            atree = ActivityTree.objects.get(user=ula.user, root_activity=ula.learning_activity.root)
        else:
            atree = ActivityTree.objects.get(user=ula.user, root_activity=ula.learning_activity)


        if atree.current_activity:
            return atree.current_activity
        else:
            return None



    def exit(self, ula, progress_status=None, objective_status=None, objective_measure=None):

        atree = ActivityTree.objects.get(user=ula.user, root_activity=ula.learning_activity.get_root())

        if not ula.is_current:
            raise NotAllowed('Set Current', "Can only exit a current activity")
        else:
            ula.is_current = False
            atree.current_activity = None
            if progress_status:
                ula.progress_status = progress_status
            if objective_status:
                ula.objective_status = objective_status
            if objective_measure is not None:
                ula.objective_measure = objective_measure
            ula.last_visited = datetime.datetime.now()
            ula.num_attempts += 1
            ula.save()
            atree.save()
            ula.rollup_rules()

    def update(self, ula, progress_status=None, objective_status=None, objective_measure=None):
        if not ula.is_current:
            raise NotAllowed('Update', "Can only update a current activity")
        else:
            if progress_status is not None:
                ula.progress_status = progress_status
            if objective_status is not None :
                ula.objective_status = objective_status
            if objective_measure is not None:
                ula.objective_measure = objective_measure
            ula.last_visited = datetime.datetime.now()
            ula.num_attempts += 1
            ula.save()

    def suspend(self, user, activity):
        pass

    def resume(self, user, activity):
        pass

    def assignActivityTree(self, user, activity):
        #Only root activities can be assigned
        if activity.parent is None:
            #If Root bring a List of all child nodes recursive
            nodeList = activity.get_children(recursive=True)
            #Plus root
            nodeList.append(activity)
            #Create another tree of UserLearningActiviy instances
            #All init at default values
            for node in nodeList:
                ula = UserLearningActivity(user=user, learning_activity=node)
                ula.save()
            #Create an instance of ActivityTree
            atree = ActivityTree(user=user, root_activity=activity)
            atree.save()
        else:
            raise NotAllowed('Assign Activity Tree', "Only Root Nodes can be assigned")

    def get_next(self, ula):

        current = self.get_current(ula)

        if current:
            nav = self.get_nav(ula)
            XML = self.nav_to_xml(root=nav)
            eroot = etree.XML(XML)
            navlist = [e for e in eroot.iter()]
            current_found = False
            for i, item in enumerate(navlist):
                if (item.get("uri") == current.learning_activity.uri) or current_found:
                    current_found = True
                    if i + 1 >= len(navlist):
                        return None
                    next = navlist[i + 1]

                    if next.get("is_container") == "False" and next.get("pre_condition") <> "disabled":
                        return next.get("uri")
            return None
        else:
            return None

    def get_prev(self, ula):

        current = self.get_current(ula)

        if current:
            nav = self.get_nav(ula)
            XML = self.nav_to_xml(root=nav)
            eroot = etree.XML(XML)
            navlist = [e for e in eroot.iter()]
            navlist.reverse()
            current_found = False
            for i, item in enumerate(navlist):
                if (item.get("uri") == current.learning_activity.uri) or current_found:
                    current_found = True
                    if i + 1 >= len(navlist):
                        return None
                    next = navlist[i + 1]

                    if next.get("is_container") == "False" and next.get("pre_condition") <> "disabled":
                        return next.get("uri")
            return None
        else:
            return None


    def get_nav(self, ula):
        #TO DO: Check is root
        #If nodes is None we are at root
        if ula.learning_activity.parent is None:
            #Refresh root in case it was changed elsewhere
            ula = UserLearningActivity.objects.get(id=ula.id)
            ula.children = []
        #Get children activities
        children = ula.get_children(recursive=False)
        if children:
            #Process child nodes
            for child in children:
                child.children = []
                child.eval_pre_condition_rule()

                #IF Parent ForwardOnly is True, disable if already tried
                #print child.learning_activity.uri, child.pre_condition
                if child.pre_condition == 'stopForwardTraversal':
                    ula.children.append(child)
                    return ula
                elif child.pre_condition == 'skip':
                    pass
                elif ula.learning_activity.forward_only and child.num_attempts > 0:
                    child.pre_condition = 'disabled'
                    ula.children.append(self.get_nav(child))
                else:
                    # disabled, hidden are still returned
                    ula.children.append(self.get_nav(child))
            return ula
        else:

            #no more nodes to process return nodes
            ula.children = []
            return ula


    def nav_to_xml(self, node=None, s="", root=None):
        open_tag_template = '<item activity = "%s"  uri = "%s"   identifier = "%s" is_current = "%s" is_container  = "%s" pre_condition = "%s"  recomended_value = "%s" objective_status ="%s" objective_measure ="%s" is_visible ="%s">'
        single_tag_template = '<item activity = "%s" uri = "%s" identifier = "%s" is_current = "%s" is_container  = "%s" pre_condition = "%s"  recomended_value = "%s" objective_status ="%s" objective_measure ="%s" is_visible ="%s"/>'

        if node is None:
            node = root
        vals = (node.learning_activity.id, node.learning_activity.uri, node.learning_activity.name, node.is_current,
                node.learning_activity.is_container, node.pre_condition,
                node.recommendation_value,
                node.objective_status, node.objective_measure,node.learning_activity.is_visible)
        if len(node.children) > 0:

            s += open_tag_template % vals
            for child in node.children:
                s += self.nav_to_xml(node=child)
            s += '</item>'
            return s
        else:
            s += single_tag_template % vals
            return s

    def nav_to_html(self, ula):
        nav_options = self.get_nav(ula)
        nav_xml = self.nav_to_xml(root=nav_options)
        xslt_root = etree.XML(TRANSFORM)
        transform = etree.XSLT(xslt_root)
        root = etree.XML(nav_xml)
        result = transform(root)
        return unicode(result)

        #from Ft.Xml.Xslt import Processor
        #processor = Processor.Processor()

        #from Ft.Xml import InputSource
        #transform = InputSource.DefaultFactory.fromString(TRANSFORM, "http://spam.com/identity.xslt")
        #source = InputSource.DefaultFactory.fromString(str(nav),"http://spam.com/doc.xml")
        #processor.appendStylesheet(transform)
        #return processor.run(source)
        
