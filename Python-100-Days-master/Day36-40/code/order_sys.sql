-- transaction table
CREATE TABLE `transaction` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_sn` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Order number',
  `member_id` bigint(20) NOT NULL COMMENT 'Transaction user ID',
  `amount` decimal(8,2) NOT NULL COMMENT 'Transaction amount',
  `integral` int(11) NOT NULL DEFAULT '0' COMMENT 'Integral used',
  `pay_state` tinyint(4) NOT NULL COMMENT 'payment type 0: balance 1: WeChat 2: Alipay 3: xxx',
  `source` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Payment source wx app web wap',
  `status` tinyint(4) NOT NULL DEFAULT '0' COMMENT 'Payment status -1: Cancel 0 Incomplete 1 Completed -2: Exception',
  `completion_time` int(11) NOT NULL COMMENT 'transaction completion time',
  `note` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Note',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `transaction_order_sn_member_id_pay_state_source_status_index` (`order_sn`(191),`member_id`,`pay_state`,`source`(191),`status`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- transaction record table
CREATE TABLE `transaction_record` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_sn` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `events` text COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Event details',
  `result` text COLLATE utf8mb4_unicode_ci COMMENT 'Result details',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- order form
CREATE TABLE `order` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_no` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Order number',
  `order_sn` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'transaction number',
  `member_id` int(11) NOT NULL COMMENT 'Customer ID',
  `supplier_id` int(11) NOT NULL COMMENT 'merchant code',
  `supplier_name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'business name',
  `order_status` tinyint(4) NOT NULL DEFAULT '0' COMMENT 'Order status 0 unpaid, 1 paid, 2 shipped, 3 signed, -1 return application, -2 returning, -3 returned, - 4 Cancel transaction',
  `after_status` tinyint(4) NOT NULL DEFAULT '0' COMMENT 'User's after-sale status 0 did not initiate after-sale 1 applied for after-sale -1 after-sale has been cancelled 2 is being processed 200 has been processed',
  `product_count` int(11) NOT NULL DEFAULT '0' COMMENT 'Product count',
  `product_amount_total` decimal(12,4) NOT NULL COMMENT 'Product total price',
  `order_amount_total` decimal(12,4) NOT NULL DEFAULT '0.0000' COMMENT 'Actual payment amount',
  `logistics_fee` decimal(12,4) NOT NULL COMMENT 'Freight amount',
  `address_id` int(11) NOT NULL COMMENT 'Receipt address code',
  `pay_channel` tinyint(4) NOT NULL DEFAULT '0' COMMENT 'Payment channel 0 balance 1 WeChat 2 Alipay',
  `out_trade_no` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Order payment order number',
  `escrow_trade_no` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Third party payment serial number',
  `pay_time` int(11) NOT NULL DEFAULT '0' COMMENT 'Payment time',
  `delivery_time` int(11) NOT NULL DEFAULT '0' COMMENT 'Delivery time',
  `order_settlement_status` tinyint(4) NOT NULL DEFAULT '0' COMMENT 'order settlement status 0 unsettled 1 settled',
  `order_settlement_time` int(11) NOT NULL DEFAULT '0' COMMENT 'Order settlement time',
  `is_package` enum('0','1') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '0' COMMENT 'Is it a package',
  `is_integral` enum('0','1') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '0' COMMENT 'Is it an integral product',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_order_sn_unique` (`order_sn`),
  KEY `order_order_sn_member_id_order_status_out_trade_no_index` (`order_sn`,`member_id`,`order_status`,`out_trade_no`(191))
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- After-sales application form
CREATE TABLE `order_returns_apply` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_no` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Order number',
  `order_detail_id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Sub-order code',
  `return_no` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'After-sale tracking number',
  `member_id` int(11) NOT NULL COMMENT 'User ID',
  `state` tinyint(4) NOT NULL COMMENT 'type 0 refund only 1 return refund',
  `product_status` tinyint(4) NOT NULL DEFAULT '0' COMMENT 'Goods status 0: Goods received 1: Goods not received',
  `why` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Return or exchange reason',
  `status` tinyint(4) NOT NULL DEFAULT '0' COMMENT 'Review status -1 rejected 0 unreviewed 1 review passed',
  `audit_time` int(11) NOT NULL DEFAULT '0' COMMENT 'Audit time',
  `audit_why` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'audit reason',
  `note` text COLLATE utf8mb4_unicode_ci COMMENT 'Note',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- After-sales record sheet
CREATE TABLE `order_returns` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `returns_no` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Return number for customer inquiry',
  `order_id` int(11) NOT NULL COMMENT 'order number',
  `express_no` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Logistics number',
  `consignee_realname` varchar(255) C
  OLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Consignee's name',
  `consignee_telphone` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Consignee',
  `consignee_telphone2` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Alternate phone number',
  `consignee_address` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'shipping address',
  `consignee_zip` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'zip code',
  `logistics_type` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Logistics mode',
  `logistics_fee` decimal(12,2) NOT NULL COMMENT 'Logistics shipping fee',
  `order_logistics_status` int(11) DEFAULT NULL COMMENT 'Logistics status',
  `logistics_settlement_status` int(11) DEFAULT NULL COMMENT 'Logistics settlement status',
  `logistics_result_last` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Logistics last state description',
  `logistics_result` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Logistics description',
  `logistics_create_time` int(11) DEFAULT NULL COMMENT 'Delivery time',
  `logistics_update_time` int(11) DEFAULT NULL COMMENT 'Logistics update time',
  `logistics_settlement_time` int(11) DEFAULT NULL COMMENT 'Logistics settlement time',
  `returns_type` tinyint(4) NOT NULL DEFAULT '0' COMMENT '0 full refund 1 partial refund',
  `handling_way` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'PUPAWAY:Return and put in storage;REDELIVERY:Re-shipment;RECLAIM-REDELIVERY:Do not ask for return and re-shipment; REFUND:Refund; COMPENSATION:No return and compensation',
  `returns_amount` decimal(8,2) NOT NULL COMMENT 'refund amount',
  `return_submit_time` int(11) NOT NULL COMMENT 'Return application time',
  `handling_time` int(11) NOT NULL COMMENT 'Return processing time',
  `remark` text COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Return reason',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- evaluation form
CREATE TABLE `order_appraise` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL COMMENT 'Order code',
  `info` text COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'comment content',
  `level` enum('-1','0','1') COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'level -1 bad 0 moderate 1 good',
  `desc_star` tinyint(4) NOT NULL COMMENT 'Description matches 1-5',
  `logistics_star` tinyint(4) NOT NULL COMMENT 'Logistics service 1-5',
  `attitude_star` tinyint(4) NOT NULL COMMENT 'Service attitude 1-5',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `order_appraise_order_id_index` (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;