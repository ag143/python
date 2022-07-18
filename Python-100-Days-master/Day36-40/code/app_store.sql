create table `app_info` (
`id` bigint(20) not null auto_increment comment 'Auto increment id, app id',
`app_name` varchar(255) default '' comment 'name',
`icon_url` varchar(255) default '' comment 'icon address',
`version` varchar(32) default '' comment 'version number',
`app_size` varchar(32) default '' comment 'Package size',
`banner_info` varchar(4096) default '' comment 'banner information',
`developer_id` varchar(255) default '' comment 'developer id',
`summary` varchar(512) default '' comment 'Introduction',
`app_desc` text comment 'Details',
`download_url` varchar(255) default '' comment 'download link',
`price` int(10) default '0' comment 'price, unit: cent',
`status` tinyint(4) unsigned default '0' comment 'Status, 1: pending review, 2: approved, 3, offline',
`version_desc` varchar(4096) default '' comment '',
`create_time` datetime not null default '0000-00-00 00:00:00' comment 'create time',
`update_time` datetime not null default '0000-00-00 00:00:00' comment 'Update time',
primary key (`id`),
key `idx_app_name` (`app_name`),
key `idx_developer` (`user_id`)
) engine=innodb auto_increment=100000 default charset=utf8 comment='app basic information table';

create table `app_ext_info` (
`id` bigint(20) not null auto_increment comment 'Auto increment id',
`app_id` bigint(20) not null default '0' comment 'app_id',
`install_count` bigint(20) unsigned not null default '0' comment 'app installs',
`score` int(10) unsigned not null default '0' comment 'score',
`comment_count` int(10) unsigned not null default '0' comment 'comment count',
`create_time` int(10) not null default 0 comment 'create time',
`update_time` int(10) not null default 0 comment 'update time',
primary key (`id`),
unique key `idx_app_id` (`app_id`)
) engine=innodb default charset=utf8 comment='App extension information table';

create table `app_category` (
`id` bigint(20) not null auto_increment comment 'Auto increment id',
`parent_id` bigint(20) not null default '0' comment 'parent category id',
`name` varchar(64) not null default '' comment 'Category name',
`icon` varchar(512) not null default '' comment 'icon address',
`category_desc` text comment 'category description',
`category_level` tinyint(4) unsigned not null default '0' comment 'category level',
`status` tinyint(4) unsigned not null default '0' comment 'Current status, 1: in use, hidden',
`display_order` int(10) unsigned not null default '0' comment 'Order, the larger the value, the higher the front',
`create_time` int(10) not null default 0 comment 'create time',
`update_time` int(10) not null default 0 comment 'update time',
primary key (`id`)
) engine=innodb default charset=utf8 comment='Classification information table';

create table `app_category_rel` (
`id` bigint(20) not null auto_increment comment 'Auto increment id',
`app_id` bigint(20) not null default '0' comment 'app_id',
`category_id` bigint(20) unsigned not null default '0' comment 'The lowest level category id',
primary key (`id`),
unique key `idx_category_app` (`category_id`, `app_record_id`),
key `idx_app` (`app_id`)
) engine=innodb default charset=utf8 comment='App and category association table';

create table `app_comment` (
`id` bigint(20) not null auto_increment comment 'Auto increment id',
`app_id` bigint(20) not null default '0' comment 'app_id',
`title` varchar(255) default '' comment 'Comment title',
`content` varchar(2048) default '' comment 'comment content',
`parent_id` bigint(20) default '0' comment 'parent comment id',
`commenter_uid` bigint(20) default '0' comment 'commenter user id',
`commenter_name` varchar(255) default '' comment 'commenter user name',
`commenter_avatar` varchar(255) default '' comment 'Commenter avatar',
`top_flag` tinyint(4) default '0' comment 'whether to top',
`like_count` int(10) default '0' comment 'The number of likes in the comment',
`status` tinyint(4) default '0' comment 'Comment status',
`create_time` int(10) not null default 0 comment 'create time',
`update_time` int(10) not null default 0 comment 'update time',
primary key (`id`),
key `idx_app_status` (`app_id`, `status`, `top_flag`)
) engine=innodb default charset=utf8 comment='Comment information table';

create table `user_app_relation` (
`id` bigint(20) not null auto_increment comment 'Auto increment id',
`user_id` bigint(20) unsigned not null default '0' comment 'user id',
`app_id` bigint(20) not null default '0' comment 'app_id',
`create_time` int(10) not null default 0 comment 'create time',
`update_time` int(10) not null default 0 comment 'update time',
`is_del` tinyint(4) not null default '0' comment '1: delete 0: not delete',
primary key (`id`),
key `idx_user_app` (`user_id`, `app_id`)
) engine=innodb auto_increment=8063 default charset=utf8 comment='User purchase relation table';

create table `bot_score` (
`id` bigint(20) not null auto_increment comment 'Auto increment id',
`app_id` bigint(20) not null default '0' comment 'app_id',
`score` int(10) default '0' comment 'User Score',
`commenter_uid` bigint(20) default '0' comment 'Rating user id',
`status` tinyint(4) default '0' comment 'rating status',
`create_time` int(10) not null default 0 comment 'create time',
`update_time` int(10) not null default 0 comment 'update time',
primary key (`id`),
unique key `idx_uid_score` (`app_id`, `commenter_uid`)
) engine=innodb default charset=utf8 comment='App rating table';