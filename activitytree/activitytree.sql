ALTER TABLE activitytree_userprofile
  DROP CONSTRAINT activitytree_userprofile_user_id_fkey;


ALTER TABLE activitytree_userprofile ADD CONSTRAINT "fk_cascade"
FOREIGN KEY (user_id) REFERENCES auth_user ON DELETE cascade;

CREATE OR REPLACE VIEW activitytree_ula_vw
as
  SELECT ul.user_id, ul.learning_activity_id, ul.pre_condition, ul.progress_status, ul.objective_status, ul.objective_measure, la.parent_id, la.rollup_objective, la.rollup_progress,la.name
   FROM activitytree_learningactivity la
   JOIN activitytree_userlearningactivity ul ON la.id = ul.learning_activity_id;

ALTER TABLE activitytree_ula_vw OWNER TO django;