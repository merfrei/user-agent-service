CREATE TABLE user_agents (
       id serial PRIMARY KEY,
       string varchar(500) NOT NULL UNIQUE,
       software varchar(64),
       os varchar(64),
       platform varchar(32) CHECK (platform IN ('desktop', 'mobile')));

CREATE INDEX user_agents_software_ix ON user_agents (software) WHERE software IS NOT NULL;
CREATE INDEX user_agents_os_ix ON user_agents (os) WHERE os IS NOT NULL;
CREATE INDEX user_agents_platform_ix ON user_agents (platform) WHERE platform IS NOT NULL;
