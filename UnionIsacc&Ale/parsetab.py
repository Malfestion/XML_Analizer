
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BASIC_INFORMATION_CLOSE BASIC_INFORMATION_OPEN COMMENT_OPEN COMPONENT_CATEGORIES_CLOSE COMPONENT_CATEGORIES_OPEN COMPONENT_CATEGORY_CLOSE COMPONENT_CATEGORY_OPEN COMPONENT_NAME_CLOSE COMPONENT_NAME_OPEN COMPONENT_OVERVIEW_CLOSE COMPONENT_OVERVIEW_OPEN GENERAL_CLOSE GENERAL_COMMENT ID INTERACTION_ID INTRINSICAL_PROPERTIES_CLOSE INTRINSICAL_PROPERTIES_OPEN LINKED_NODE_CLOSE LINKED_NODE_OPEN MODEL_NODES_CLOSE MODEL_NODES_OPEN MODEL_NODE_CLOSE MODEL_NODE_OPEN NODE_ID OFFICE_DOCUMENT_CLOSE OFFICE_DOCUMENT_OPEN OFFICE_MODEL_CLOSE OFFICE_MODEL_OPEN PEER_OBJECTIVE_CLOSE PEER_OBJECTIVE_OPEN POLICY_DESCRIPTION_CLOSE POLICY_DESCRIPTION_OPEN POLICY_ID POLICY_NAME_CLOSE POLICY_NAME_OPEN PROPERTIES_COLOR_CLOSE PROPERTIES_COLOR_OPEN PROPERTIES_HEIGHT_CLOSE PROPERTIES_HEIGHT_OPEN PROPERTIES_MATERIAL_CLOSE PROPERTIES_MATERIAL_OPEN PROPERTIES_OTHER_CLOSE PROPERTIES_OTHER_OPEN PROPERTIES_WEIGHT_CLOSE PROPERTIES_WEIGHT_OPEN RELATIONSHIP_TYPE_CLOSE RELATIONSHIP_TYPE_OPEN SECURITY_OBJECTIVES_CLOSE SECURITY_OBJECTIVES_OPEN SECURITY_OBJECTIVE_CLOSE SECURITY_OBJECTIVE_OPEN SECURITY_POLICIES_CLOSE SECURITY_POLICIES_OPEN SECURITY_POLICY_CLOSE SECURITY_POLICY_OPEN SECURITY_RELATIONSHIP_CLOSE SECURITY_RELATIONSHIP_OPEN SELF_OBJECTIVE_CLOSE SELF_OBJECTIVE_OPEN SP_ADDITIONAL_INFORMATION_CLOSE SP_ADDITIONAL_INFORMATION_OPEN SP_COMMENT_CLOSE SP_COMMENT_OPEN SP_OBJECTIVES_CLOSE SP_OBJECTIVES_OPEN SP_OBJECTIVE_CLOSE SP_OBJECTIVE_OPEN STRING THREATS_CLOSE THREATS_OPEN THREAT_CLOSE THREAT_DESCRIPTION_CLOSE THREAT_DESCRIPTION_OPEN THREAT_NAME_CLOSE THREAT_NAME_OPEN THREAT_OPEN THREAT_VULNERABILITIES_CLOSE THREAT_VULNERABILITIES_OPEN VULNERABILITIES_VULNERABILITY_CLOSE VULNERABILITIES_VULNERABILITY_OPEN XML_VERSION\n    doc_model : XML_VERSION  doc_model\n              | doc_comment doc_model\n              | OFFICE_DOCUMENT_OPEN office_model OFFICE_DOCUMENT_CLOSE\n    \n    office_model : OFFICE_MODEL_OPEN model_nodes OFFICE_MODEL_CLOSE\n    \n    model_nodes : MODEL_NODES_OPEN model_node model_nodes\n                | model_node model_nodes\n                | MODEL_NODES_CLOSE\n    \n    model_node : MODEL_NODE_OPEN model_node\n               | basic_info model_node\n               | threats model_node\n\t\t\t   | structure_security_policies model_node\n\t\t\t   | structure_security_relationships model_node\n               | MODEL_NODE_CLOSE\n    \n    basic_info : BASIC_INFORMATION_OPEN basic_info\n               | component_name basic_info\n               | component_overview basic_info\n               | component_categories basic_info\n               | intrinsical_properties basic_info\n               | other_details basic_info\n               | BASIC_INFORMATION_CLOSE\n    \n    component_name : COMPONENT_NAME_OPEN str COMPONENT_NAME_CLOSE\n    \n    intrinsical_properties : INTRINSICAL_PROPERTIES_OPEN intrinsical_properties\n                           | properties_color intrinsical_properties\n                           | properties_material intrinsical_properties\n                           | properties_height intrinsical_properties\n                           | properties_weight intrinsical_properties\n                           | INTRINSICAL_PROPERTIES_CLOSE\n    \n    component_categories : COMPONENT_CATEGORIES_OPEN component_categories\n                         | component_category component_categories\n                         | COMPONENT_CATEGORIES_CLOSE\n    \n    component_overview : COMPONENT_OVERVIEW_OPEN str COMPONENT_OVERVIEW_CLOSE\n    \n    other_details : PROPERTIES_OTHER_OPEN PROPERTIES_OTHER_CLOSE\n    \n    component_category : COMPONENT_CATEGORY_OPEN COMPONENT_CATEGORY_CLOSE\n    \n    properties_color : PROPERTIES_COLOR_OPEN str PROPERTIES_COLOR_CLOSE\n    \n    properties_material : PROPERTIES_MATERIAL_OPEN str PROPERTIES_MATERIAL_CLOSE\n    \n    properties_height : PROPERTIES_HEIGHT_OPEN str PROPERTIES_HEIGHT_CLOSE\n    \n    properties_weight : PROPERTIES_WEIGHT_OPEN str PROPERTIES_WEIGHT_CLOSE\n    \n    threats : THREATS_OPEN threats\n            | threat threats\n            | THREATS_CLOSE\n    \n    threat : THREAT_OPEN threat\n            | threat_name threat\n            | threat_description threat\n            | threat_vulnerabilities threat\n            | THREAT_CLOSE\n    \n    threat_name : THREAT_NAME_OPEN str THREAT_NAME_CLOSE\n    \n    threat_description : THREAT_DESCRIPTION_OPEN str THREAT_DESCRIPTION_CLOSE\n    \n    threat_vulnerabilities : THREAT_VULNERABILITIES_OPEN threat_vulnerabilities\n                           | threat_vulnerability threat_vulnerabilities\n                           | THREAT_VULNERABILITIES_CLOSE\n    \n    threat_vulnerability : VULNERABILITIES_VULNERABILITY_OPEN str VULNERABILITIES_VULNERABILITY_CLOSE\n    \n\tstructure_security_policies : SECURITY_POLICIES_OPEN security_policies SECURITY_POLICIES_CLOSE\n\t\n\tsecurity_policies : security_policies security_policies\n\t\t\t\t\t  | security_policy\n\t\n\tsecurity_policy : SECURITY_POLICY_OPEN ID GENERAL_CLOSE POLICY_NAME_OPEN STRING POLICY_NAME_CLOSE POLICY_DESCRIPTION_OPEN STRING POLICY_DESCRIPTION_CLOSE security_objectives_SP additional_info_SP SECURITY_POLICY_CLOSE\n\t\n\tsecurity_objectives_SP : SP_OBJECTIVES_OPEN SECURITY_OBJECTIVE_OPEN STRING SECURITY_OBJECTIVE_CLOSE SP_OBJECTIVES_CLOSE\n\t\n\tadditional_info_SP : SP_ADDITIONAL_INFORMATION_OPEN SP_COMMENT_OPEN SP_COMMENT_CLOSE SP_ADDITIONAL_INFORMATION_CLOSE\n\t\n\tstructure_security_relationships : SECURITY_RELATIONSHIP_OPEN security-relationships SECURITY_RELATIONSHIP_CLOSE\n\t\n    security-relationships : security-relationships security-relationships\n                           | LINKED_NODE_OPEN ID GENERAL_CLOSE linked-node LINKED_NODE_CLOSE\n    \n    linked-node : linked-node linked-node\n                | RELATIONSHIP_TYPE_OPEN ID GENERAL_CLOSE relationship-type RELATIONSHIP_TYPE_CLOSE\n    \n    relationship-type : SECURITY_OBJECTIVES_OPEN security-objectives_SR SECURITY_OBJECTIVES_CLOSE\n    \n    security-objectives_SR : security-objectives_SR security-objectives_SR\n\t\t\t\t\t\t   | SECURITY_OBJECTIVE_OPEN security-objective_SR security-objective_SR SECURITY_OBJECTIVE_CLOSE\n    \n    security-objective_SR : SELF_OBJECTIVE_OPEN SELF_OBJECTIVE_CLOSE\n\t\t\t\t\t\t  | PEER_OBJECTIVE_OPEN PEER_OBJECTIVE_CLOSE\n    \n    doc_comment : COMMENT_OPEN doc_comment\n                | str doc_comment\n                | GENERAL_CLOSE\n    \n    str : STRING str\n              | STRING\n              |\n    '
    
_lr_action_items = {'PROPERTIES_COLOR_OPEN':([11,17,19,20,23,24,25,29,31,34,35,37,40,44,45,47,48,49,51,52,55,57,60,66,67,68,71,72,77,78,81,82,85,88,91,92,93,95,96,97,98,99,101,103,106,109,114,116,119,120,123,124,126,127,],[46,46,-30,46,-20,46,46,46,-40,46,46,46,46,46,46,46,46,46,-13,46,46,46,46,-27,-16,-19,-22,-9,-32,-26,-38,-10,-14,-24,-29,-11,-15,-8,46,-18,-28,-17,-23,-12,-25,-39,-52,-58,-31,-34,-21,-37,-35,-36,]),'THREAT_CLOSE':([11,18,21,23,25,27,31,32,33,34,35,38,44,47,48,51,57,61,63,67,68,69,72,76,81,82,85,86,87,92,93,95,96,97,99,103,107,109,110,114,116,122,125,],[18,-45,18,-20,18,18,-40,-50,18,18,18,18,18,18,18,-13,18,18,18,-16,-19,-43,-9,-42,-38,-10,-14,-41,-48,-11,-15,-8,18,-18,-17,-12,-44,-39,-49,-52,-58,-47,-46,]),'VULNERABILITIES_VULNERABILITY_CLOSE':([3,12,36,84,],[-72,-71,-73,118,]),'BASIC_INFORMATION_CLOSE':([11,17,19,20,23,25,31,34,35,37,44,45,47,48,49,51,52,57,66,67,68,71,72,77,78,81,82,85,88,91,92,93,95,96,97,98,99,101,103,106,109,114,116,119,123,],[23,23,-30,23,-20,23,-40,23,23,23,23,23,23,23,23,-13,23,23,-27,-16,-19,-22,-9,-32,-26,-38,-10,-14,-24,-29,-11,-15,-8,23,-18,-28,-17,-23,-12,-25,-39,-52,-58,-31,-21,]),'COMPONENT_NAME_CLOSE':([3,12,56,102,],[-72,-71,-73,123,]),'INTRINSICAL_PROPERTIES_OPEN':([11,17,19,20,23,24,25,29,31,34,35,37,40,44,45,47,48,49,51,52,55,57,60,66,67,68,71,72,77,78,81,82,85,88,91,92,93,95,96,97,98,99,101,103,106,109,114,116,119,120,123,124,126,127,],[24,24,-30,24,-20,24,24,24,-40,24,24,24,24,24,24,24,24,24,-13,24,24,24,24,-27,-16,-19,-22,-9,-32,-26,-38,-10,-14,-24,-29,-11,-15,-8,24,-18,-28,-17,-23,-12,-25,-39,-52,-58,-31,-34,-21,-37,-35,-36,]),'LINKED_NODE_OPEN':([30,80,117,135,],[79,79,79,-60,]),'SECURITY_POLICIES_OPEN':([11,23,25,31,34,35,44,47,48,51,57,67,68,72,81,82,85,92,93,95,96,97,99,103,109,114,116,],[26,-20,26,-40,26,26,26,26,26,-13,26,-16,-19,-9,-38,-10,-14,-11,-15,-8,26,-18,-17,-12,-39,-52,-58,]),'THREAT_NAME_CLOSE':([3,12,59,105,],[-72,-71,-73,125,]),'SECURITY_POLICY_CLOSE':([159,167,],[163,-57,]),'SECURITY_RELATIONSHIP_OPEN':([11,23,25,31,34,35,44,47,48,51,57,67,68,72,81,82,85,92,93,95,96,97,99,103,109,114,116,],[30,-20,30,-40,30,30,30,30,30,-13,30,-16,-19,-9,-38,-10,-14,-11,-15,-8,30,-18,-17,-12,-39,-52,-58,]),'THREATS_CLOSE':([11,18,23,25,31,33,34,35,44,47,48,51,57,63,67,68,69,72,76,81,82,85,86,92,93,95,96,97,99,103,107,109,114,116,],[31,-45,-20,31,-40,31,31,31,31,31,31,-13,31,31,-16,-19,-43,-9,-42,-38,-10,-14,-41,-11,-15,-8,31,-18,-17,-12,-44,-39,-52,-58,]),'PROPERTIES_HEIGHT_CLOSE':([3,12,65,111,],[-72,-71,-73,127,]),'SP_COMMENT_CLOSE':([162,],[165,]),'POLICY_DESCRIPTION_OPEN':([137,],[139,]),'SECURITY_OBJECTIVES_CLOSE':([143,147,160,],[148,-64,-65,]),'COMPONENT_OVERVIEW_CLOSE':([3,12,42,90,],[-72,-71,-73,119,]),'SECURITY_RELATIONSHIP_CLOSE':([80,117,135,],[116,-59,-60,]),'THREATS_OPEN':([11,18,23,25,31,33,34,35,44,47,48,51,57,63,67,68,69,72,76,81,82,85,86,92,93,95,96,97,99,103,107,109,114,116,],[33,-45,-20,33,-40,33,33,33,33,33,33,-13,33,33,-16,-19,-43,-9,-42,-38,-10,-14,-41,-11,-15,-8,33,-18,-17,-12,-44,-39,-52,-58,]),'OFFICE_DOCUMENT_OPEN':([0,1,5,8,13,15,],[2,2,2,-70,-68,-69,]),'PROPERTIES_MATERIAL_OPEN':([11,17,19,20,23,24,25,29,31,34,35,37,40,44,45,47,48,49,51,52,55,57,60,66,67,68,71,72,77,78,81,82,85,88,91,92,93,95,96,97,98,99,101,103,106,109,114,116,119,120,123,124,126,127,],[62,62,-30,62,-20,62,62,62,-40,62,62,62,62,62,62,62,62,62,-13,62,62,62,62,-27,-16,-19,-22,-9,-32,-26,-38,-10,-14,-24,-29,-11,-15,-8,62,-18,-28,-17,-23,-12,-25,-39,-52,-58,-31,-34,-21,-37,-35,-36,]),'SP_ADDITIONAL_INFORMATION_OPEN':([153,166,],[158,-56,]),'COMMENT_OPEN':([0,1,3,4,5,7,8,12,13,15,],[4,4,-72,4,4,4,-70,-71,-68,-69,]),'THREAT_VULNERABILITIES_OPEN':([11,18,21,23,25,27,31,32,33,34,35,38,39,44,47,48,51,57,61,63,64,67,68,69,72,76,81,82,85,86,87,92,93,95,96,97,99,103,107,109,110,114,116,118,122,125,],[39,-45,39,-20,39,39,-40,-50,39,39,39,39,39,39,39,39,-13,39,39,39,39,-16,-19,-43,-9,-42,-38,-10,-14,-41,-48,-11,-15,-8,39,-18,-17,-12,-44,-39,-49,-52,-58,-51,-47,-46,]),'OFFICE_DOCUMENT_CLOSE':([10,70,],[16,-4,]),'COMPONENT_CATEGORIES_CLOSE':([11,17,19,20,23,25,31,34,35,37,43,44,45,47,48,49,50,51,52,57,66,67,68,71,72,77,78,81,82,85,88,89,91,92,93,95,96,97,98,99,101,103,106,109,114,116,119,123,],[19,19,-30,19,-20,19,-40,19,19,19,19,19,19,19,19,19,19,-13,19,19,-27,-16,-19,-22,-9,-32,-26,-38,-10,-14,-24,-33,-29,-11,-15,-8,19,-18,-28,-17,-23,-12,-25,-39,-52,-58,-31,-21,]),'POLICY_NAME_CLOSE':([133,],[137,]),'RELATIONSHIP_TYPE_OPEN':([129,132,136,145,],[131,131,131,-62,]),'BASIC_INFORMATION_OPEN':([11,17,19,20,23,25,31,34,35,37,44,45,47,48,49,51,52,57,66,67,68,71,72,77,78,81,82,85,88,91,92,93,95,96,97,98,99,101,103,106,109,114,116,119,123,],[37,37,-30,37,-20,37,-40,37,37,37,37,37,37,37,37,-13,37,37,-27,-16,-19,-22,-9,-32,-26,-38,-10,-14,-24,-29,-11,-15,-8,37,-18,-28,-17,-23,-12,-25,-39,-52,-58,-31,-21,]),'THREAT_OPEN':([11,18,21,23,25,27,31,32,33,34,35,38,44,47,48,51,57,61,63,67,68,69,72,76,81,82,85,86,87,92,93,95,96,97,99,103,107,109,110,114,116,122,125,],[38,-45,38,-20,38,38,-40,-50,38,38,38,38,38,38,38,-13,38,38,38,-16,-19,-43,-9,-42,-38,-10,-14,-41,-48,-11,-15,-8,38,-18,-17,-12,-44,-39,-49,-52,-58,-47,-46,]),'VULNERABILITIES_VULNERABILITY_OPEN':([11,18,21,23,25,27,31,32,33,34,35,38,39,44,47,48,51,57,61,63,64,67,68,69,72,76,81,82,85,86,87,92,93,95,96,97,99,103,107,109,110,114,116,118,122,125,],[36,-45,36,-20,36,36,-40,-50,36,36,36,36,36,36,36,36,-13,36,36,36,36,-16,-19,-43,-9,-42,-38,-10,-14,-41,-48,-11,-15,-8,36,-18,-17,-12,-44,-39,-49,-52,-58,-51,-47,-46,]),'COMPONENT_CATEGORY_OPEN':([11,17,19,20,23,25,31,34,35,37,43,44,45,47,48,49,50,51,52,57,66,67,68,71,72,77,78,81,82,85,88,89,91,92,93,95,96,97,98,99,101,103,106,109,114,116,119,123,],[41,41,-30,41,-20,41,-40,41,41,41,41,41,41,41,41,41,41,-13,41,41,-27,-16,-19,-22,-9,-32,-26,-38,-10,-14,-24,-33,-29,-11,-15,-8,41,-18,-28,-17,-23,-12,-25,-39,-52,-58,-31,-21,]),'SP_OBJECTIVES_OPEN':([146,],[152,]),'THREAT_DESCRIPTION_CLOSE':([3,12,53,100,],[-72,-71,-73,122,]),'COMPONENT_OVERVIEW_OPEN':([11,17,19,20,23,25,31,34,35,37,44,45,47,48,49,51,52,57,66,67,68,71,72,77,78,81,82,85,88,91,92,93,95,96,97,98,99,101,103,106,109,114,116,119,123,],[42,42,-30,42,-20,42,-40,42,42,42,42,42,42,42,42,-13,42,42,-27,-16,-19,-22,-9,-32,-26,-38,-10,-14,-24,-29,-11,-15,-8,42,-18,-28,-17,-23,-12,-25,-39,-52,-58,-31,-21,]),'PROPERTIES_WEIGHT_CLOSE':([3,12,58,104,],[-72,-71,-73,124,]),'$end':([6,9,14,16,],[0,-1,-2,-3,]),'POLICY_DESCRIPTION_CLOSE':([142,],[146,]),'XML_VERSION':([0,1,5,8,13,15,],[1,1,1,-70,-68,-69,]),'SECURITY_OBJECTIVE_CLOSE':([154,155,156,161,],[-67,160,-66,164,]),'PROPERTIES_COLOR_CLOSE':([3,12,46,94,],[-72,-71,-73,120,]),'STRING':([0,1,3,4,5,7,8,12,13,15,36,42,46,53,56,58,59,62,65,130,139,157,],[3,3,3,3,3,3,-70,-71,-68,-69,3,3,3,3,3,3,3,3,3,133,142,161,]),'SECURITY_POLICY_OPEN':([26,73,75,113,163,],[74,-54,74,74,-55,]),'PEER_OBJECTIVE_CLOSE':([149,],[154,]),'MODEL_NODES_OPEN':([11,35,51,72,82,92,95,96,103,],[48,48,-13,-9,-10,-11,-8,48,-12,]),'LINKED_NODE_CLOSE':([132,136,145,],[135,-61,-62,]),'PROPERTIES_HEIGHT_OPEN':([11,17,19,20,23,24,25,29,31,34,35,37,40,44,45,47,48,49,51,52,55,57,60,66,67,68,71,72,77,78,81,82,85,88,91,92,93,95,96,97,98,99,101,103,106,109,114,116,119,120,123,124,126,127,],[65,65,-30,65,-20,65,65,65,-40,65,65,65,65,65,65,65,65,65,-13,65,65,65,65,-27,-16,-19,-22,-9,-32,-26,-38,-10,-14,-24,-29,-11,-15,-8,65,-18,-28,-17,-23,-12,-25,-39,-52,-58,-31,-34,-21,-37,-35,-36,]),'THREAT_VULNERABILITIES_CLOSE':([11,18,21,23,25,27,31,32,33,34,35,38,39,44,47,48,51,57,61,63,64,67,68,69,72,76,81,82,85,86,87,92,93,95,96,97,99,103,107,109,110,114,116,118,122,125,],[32,-45,32,-20,32,32,-40,-50,32,32,32,32,32,32,32,32,-13,32,32,32,32,-16,-19,-43,-9,-42,-38,-10,-14,-41,-48,-11,-15,-8,32,-18,-17,-12,-44,-39,-49,-52,-58,-51,-47,-46,]),'COMPONENT_CATEGORIES_OPEN':([11,17,19,20,23,25,31,34,35,37,43,44,45,47,48,49,50,51,52,57,66,67,68,71,72,77,78,81,82,85,88,89,91,92,93,95,96,97,98,99,101,103,106,109,114,116,119,123,],[50,50,-30,50,-20,50,-40,50,50,50,50,50,50,50,50,50,50,-13,50,50,-27,-16,-19,-22,-9,-32,-26,-38,-10,-14,-24,-33,-29,-11,-15,-8,50,-18,-28,-17,-23,-12,-25,-39,-52,-58,-31,-21,]),'MODEL_NODE_CLOSE':([11,23,25,31,34,35,44,47,48,51,57,67,68,72,81,82,85,92,93,95,96,97,99,103,109,114,116,],[51,-20,51,-40,51,51,51,51,51,-13,51,-16,-19,-9,-38,-10,-14,-11,-15,-8,51,-18,-17,-12,-39,-52,-58,]),'THREAT_DESCRIPTION_OPEN':([11,18,21,23,25,27,31,32,33,34,35,38,44,47,48,51,57,61,63,67,68,69,72,76,81,82,85,86,87,92,93,95,96,97,99,103,107,109,110,114,116,122,125,],[53,-45,53,-20,53,53,-40,-50,53,53,53,53,53,53,53,-13,53,53,53,-16,-19,-43,-9,-42,-38,-10,-14,-41,-48,-11,-15,-8,53,-18,-17,-12,-44,-39,-49,-52,-58,-47,-46,]),'SELF_OBJECTIVE_CLOSE':([151,],[156,]),'RELATIONSHIP_TYPE_CLOSE':([141,148,],[145,-63,]),'MODEL_NODES_CLOSE':([11,35,51,72,82,92,95,96,103,],[54,54,-13,-9,-10,-11,-8,54,-12,]),'GENERAL_CLOSE':([0,1,3,4,5,7,8,12,13,15,112,115,134,],[8,8,-72,8,8,8,-70,-71,-68,-69,128,129,138,]),'ID':([74,79,131,],[112,115,134,]),'COMPONENT_NAME_OPEN':([11,17,19,20,23,25,31,34,35,37,44,45,47,48,49,51,52,57,66,67,68,71,72,77,78,81,82,85,88,91,92,93,95,96,97,98,99,101,103,106,109,114,116,119,123,],[56,56,-30,56,-20,56,-40,56,56,56,56,56,56,56,56,-13,56,56,-27,-16,-19,-22,-9,-32,-26,-38,-10,-14,-24,-29,-11,-15,-8,56,-18,-28,-17,-23,-12,-25,-39,-52,-58,-31,-21,]),'SECURITY_OBJECTIVES_OPEN':([138,],[140,]),'OFFICE_MODEL_CLOSE':([22,54,83,121,],[70,-7,-6,-5,]),'PROPERTIES_WEIGHT_OPEN':([11,17,19,20,23,24,25,29,31,34,35,37,40,44,45,47,48,49,51,52,55,57,60,66,67,68,71,72,77,78,81,82,85,88,91,92,93,95,96,97,98,99,101,103,106,109,114,116,119,120,123,124,126,127,],[58,58,-30,58,-20,58,58,58,-40,58,58,58,58,58,58,58,58,58,-13,58,58,58,58,-27,-16,-19,-22,-9,-32,-26,-38,-10,-14,-24,-29,-11,-15,-8,58,-18,-28,-17,-23,-12,-25,-39,-52,-58,-31,-34,-21,-37,-35,-36,]),'THREAT_NAME_OPEN':([11,18,21,23,25,27,31,32,33,34,35,38,44,47,48,51,57,61,63,67,68,69,72,76,81,82,85,86,87,92,93,95,96,97,99,103,107,109,110,114,116,122,125,],[59,-45,59,-20,59,59,-40,-50,59,59,59,59,59,59,59,-13,59,59,59,-16,-19,-43,-9,-42,-38,-10,-14,-41,-48,-11,-15,-8,59,-18,-17,-12,-44,-39,-49,-52,-58,-47,-46,]),'SP_OBJECTIVES_CLOSE':([164,],[166,]),'OFFICE_MODEL_OPEN':([2,],[11,]),'SECURITY_OBJECTIVE_OPEN':([140,143,147,152,160,],[144,144,144,157,-65,]),'POLICY_NAME_OPEN':([128,],[130,]),'PEER_OBJECTIVE_OPEN':([144,150,154,156,],[149,149,-67,-66,]),'PROPERTIES_OTHER_OPEN':([11,17,19,20,23,25,31,34,35,37,44,45,47,48,49,51,52,57,66,67,68,71,72,77,78,81,82,85,88,91,92,93,95,96,97,98,99,101,103,106,109,114,116,119,123,],[28,28,-30,28,-20,28,-40,28,28,28,28,28,28,28,28,-13,28,28,-27,-16,-19,-22,-9,-32,-26,-38,-10,-14,-24,-29,-11,-15,-8,28,-18,-28,-17,-23,-12,-25,-39,-52,-58,-31,-21,]),'SP_COMMENT_OPEN':([158,],[162,]),'PROPERTIES_MATERIAL_CLOSE':([3,12,62,108,],[-72,-71,-73,126,]),'SECURITY_POLICIES_CLOSE':([73,75,113,163,],[-54,114,-53,-55,]),'MODEL_NODE_OPEN':([11,23,25,31,34,35,44,47,48,51,57,67,68,72,81,82,85,92,93,95,96,97,99,103,109,114,116,],[47,-20,47,-40,47,47,47,47,47,-13,47,-16,-19,-9,-38,-10,-14,-11,-15,-8,47,-18,-17,-12,-39,-52,-58,]),'COMPONENT_CATEGORY_CLOSE':([41,],[89,]),'PROPERTIES_OTHER_CLOSE':([28,],[77,]),'SP_ADDITIONAL_INFORMATION_CLOSE':([165,],[167,]),'SELF_OBJECTIVE_OPEN':([144,150,154,156,],[151,151,-67,-66,]),'INTRINSICAL_PROPERTIES_CLOSE':([11,17,19,20,23,24,25,29,31,34,35,37,40,44,45,47,48,49,51,52,55,57,60,66,67,68,71,72,77,78,81,82,85,88,91,92,93,95,96,97,98,99,101,103,106,109,114,116,119,120,123,124,126,127,],[66,66,-30,66,-20,66,66,66,-40,66,66,66,66,66,66,66,66,66,-13,66,66,66,66,-27,-16,-19,-22,-9,-32,-26,-38,-10,-14,-24,-29,-11,-15,-8,66,-18,-28,-17,-23,-12,-25,-39,-52,-58,-31,-34,-21,-37,-35,-36,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'properties_weight':([11,17,20,24,25,29,34,35,37,40,44,45,47,48,49,52,55,57,60,96,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'doc_comment':([0,1,4,5,7,],[5,5,13,5,15,]),'other_details':([11,17,20,25,34,35,37,44,45,47,48,49,52,57,96,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'threat_description':([11,21,25,27,33,34,35,38,44,47,48,57,61,63,96,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'component_category':([11,17,20,25,34,35,37,43,44,45,47,48,49,50,52,57,96,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'basic_info':([11,17,20,25,34,35,37,44,45,47,48,49,52,57,96,],[25,67,68,25,25,25,85,25,93,25,25,97,99,25,25,]),'threat_vulnerabilities':([11,21,25,27,33,34,35,38,39,44,47,48,57,61,63,64,96,],[61,61,61,61,61,61,61,61,87,61,61,61,61,61,61,110,61,]),'component_overview':([11,17,20,25,34,35,37,44,45,47,48,49,52,57,96,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'security-objectives_SR':([140,143,147,],[143,147,147,]),'threats':([11,25,33,34,35,44,47,48,57,63,96,],[34,34,81,34,34,34,34,34,34,109,34,]),'model_node':([11,25,34,35,44,47,48,57,96,],[35,72,82,35,92,95,96,103,35,]),'security-objective_SR':([144,150,],[150,155,]),'properties_material':([11,17,20,24,25,29,34,35,37,40,44,45,47,48,49,52,55,57,60,96,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'additional_info_SP':([153,],[159,]),'linked-node':([129,132,136,],[132,136,136,]),'model_nodes':([11,35,96,],[22,83,121,]),'structure_security_policies':([11,25,34,35,44,47,48,57,96,],[44,44,44,44,44,44,44,44,44,]),'component_name':([11,17,20,25,34,35,37,44,45,47,48,49,52,57,96,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'str':([0,1,3,4,5,7,36,42,46,53,56,58,59,62,65,],[7,7,12,7,7,7,84,90,94,100,102,104,105,108,111,]),'doc_model':([0,1,5,],[6,9,14,]),'intrinsical_properties':([11,17,20,24,25,29,34,35,37,40,44,45,47,48,49,52,55,57,60,96,],[49,49,49,71,49,78,49,49,49,88,49,49,49,49,49,49,101,49,106,49,]),'relationship-type':([138,],[141,]),'component_categories':([11,17,20,25,34,35,37,43,44,45,47,48,49,50,52,57,96,],[52,52,52,52,52,52,52,91,52,52,52,52,52,98,52,52,52,]),'security-relationships':([30,80,117,],[80,117,117,]),'properties_color':([11,17,20,24,25,29,34,35,37,40,44,45,47,48,49,52,55,57,60,96,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'security_objectives_SP':([146,],[153,]),'security_policy':([26,75,113,],[73,73,73,]),'structure_security_relationships':([11,25,34,35,44,47,48,57,96,],[57,57,57,57,57,57,57,57,57,]),'properties_height':([11,17,20,24,25,29,34,35,37,40,44,45,47,48,49,52,55,57,60,96,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'threat_name':([11,21,25,27,33,34,35,38,44,47,48,57,61,63,96,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'office_model':([2,],[10,]),'threat':([11,21,25,27,33,34,35,38,44,47,48,57,61,63,96,],[63,69,63,76,63,63,63,86,63,63,63,63,107,63,63,]),'threat_vulnerability':([11,21,25,27,33,34,35,38,39,44,47,48,57,61,63,64,96,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'security_policies':([26,75,113,],[75,113,113,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> doc_model","S'",1,None,None,None),
  ('doc_model -> XML_VERSION doc_model','doc_model',2,'p_doc_model','TP2_entrega3.py',144),
  ('doc_model -> doc_comment doc_model','doc_model',2,'p_doc_model','TP2_entrega3.py',145),
  ('doc_model -> OFFICE_DOCUMENT_OPEN office_model OFFICE_DOCUMENT_CLOSE','doc_model',3,'p_doc_model','TP2_entrega3.py',146),
  ('office_model -> OFFICE_MODEL_OPEN model_nodes OFFICE_MODEL_CLOSE','office_model',3,'p_office_model','TP2_entrega3.py',152),
  ('model_nodes -> MODEL_NODES_OPEN model_node model_nodes','model_nodes',3,'p_model_nodes','TP2_entrega3.py',157),
  ('model_nodes -> model_node model_nodes','model_nodes',2,'p_model_nodes','TP2_entrega3.py',158),
  ('model_nodes -> MODEL_NODES_CLOSE','model_nodes',1,'p_model_nodes','TP2_entrega3.py',159),
  ('model_node -> MODEL_NODE_OPEN model_node','model_node',2,'p_model_node','TP2_entrega3.py',164),
  ('model_node -> basic_info model_node','model_node',2,'p_model_node','TP2_entrega3.py',165),
  ('model_node -> threats model_node','model_node',2,'p_model_node','TP2_entrega3.py',166),
  ('model_node -> structure_security_policies model_node','model_node',2,'p_model_node','TP2_entrega3.py',167),
  ('model_node -> structure_security_relationships model_node','model_node',2,'p_model_node','TP2_entrega3.py',168),
  ('model_node -> MODEL_NODE_CLOSE','model_node',1,'p_model_node','TP2_entrega3.py',169),
  ('basic_info -> BASIC_INFORMATION_OPEN basic_info','basic_info',2,'p_basic_information','TP2_entrega3.py',179),
  ('basic_info -> component_name basic_info','basic_info',2,'p_basic_information','TP2_entrega3.py',180),
  ('basic_info -> component_overview basic_info','basic_info',2,'p_basic_information','TP2_entrega3.py',181),
  ('basic_info -> component_categories basic_info','basic_info',2,'p_basic_information','TP2_entrega3.py',182),
  ('basic_info -> intrinsical_properties basic_info','basic_info',2,'p_basic_information','TP2_entrega3.py',183),
  ('basic_info -> other_details basic_info','basic_info',2,'p_basic_information','TP2_entrega3.py',184),
  ('basic_info -> BASIC_INFORMATION_CLOSE','basic_info',1,'p_basic_information','TP2_entrega3.py',185),
  ('component_name -> COMPONENT_NAME_OPEN str COMPONENT_NAME_CLOSE','component_name',3,'p_component_name','TP2_entrega3.py',191),
  ('intrinsical_properties -> INTRINSICAL_PROPERTIES_OPEN intrinsical_properties','intrinsical_properties',2,'p_intrinsical_properties','TP2_entrega3.py',197),
  ('intrinsical_properties -> properties_color intrinsical_properties','intrinsical_properties',2,'p_intrinsical_properties','TP2_entrega3.py',198),
  ('intrinsical_properties -> properties_material intrinsical_properties','intrinsical_properties',2,'p_intrinsical_properties','TP2_entrega3.py',199),
  ('intrinsical_properties -> properties_height intrinsical_properties','intrinsical_properties',2,'p_intrinsical_properties','TP2_entrega3.py',200),
  ('intrinsical_properties -> properties_weight intrinsical_properties','intrinsical_properties',2,'p_intrinsical_properties','TP2_entrega3.py',201),
  ('intrinsical_properties -> INTRINSICAL_PROPERTIES_CLOSE','intrinsical_properties',1,'p_intrinsical_properties','TP2_entrega3.py',202),
  ('component_categories -> COMPONENT_CATEGORIES_OPEN component_categories','component_categories',2,'p_component_categories','TP2_entrega3.py',208),
  ('component_categories -> component_category component_categories','component_categories',2,'p_component_categories','TP2_entrega3.py',209),
  ('component_categories -> COMPONENT_CATEGORIES_CLOSE','component_categories',1,'p_component_categories','TP2_entrega3.py',210),
  ('component_overview -> COMPONENT_OVERVIEW_OPEN str COMPONENT_OVERVIEW_CLOSE','component_overview',3,'p_component_overview','TP2_entrega3.py',217),
  ('other_details -> PROPERTIES_OTHER_OPEN PROPERTIES_OTHER_CLOSE','other_details',2,'p_other_details','TP2_entrega3.py',223),
  ('component_category -> COMPONENT_CATEGORY_OPEN COMPONENT_CATEGORY_CLOSE','component_category',2,'p_component_category','TP2_entrega3.py',229),
  ('properties_color -> PROPERTIES_COLOR_OPEN str PROPERTIES_COLOR_CLOSE','properties_color',3,'p_properties_color','TP2_entrega3.py',235),
  ('properties_material -> PROPERTIES_MATERIAL_OPEN str PROPERTIES_MATERIAL_CLOSE','properties_material',3,'p_properties_material','TP2_entrega3.py',241),
  ('properties_height -> PROPERTIES_HEIGHT_OPEN str PROPERTIES_HEIGHT_CLOSE','properties_height',3,'p_properties_height','TP2_entrega3.py',247),
  ('properties_weight -> PROPERTIES_WEIGHT_OPEN str PROPERTIES_WEIGHT_CLOSE','properties_weight',3,'p_properties_weight','TP2_entrega3.py',253),
  ('threats -> THREATS_OPEN threats','threats',2,'p_threats','TP2_entrega3.py',262),
  ('threats -> threat threats','threats',2,'p_threats','TP2_entrega3.py',263),
  ('threats -> THREATS_CLOSE','threats',1,'p_threats','TP2_entrega3.py',264),
  ('threat -> THREAT_OPEN threat','threat',2,'p_threat','TP2_entrega3.py',269),
  ('threat -> threat_name threat','threat',2,'p_threat','TP2_entrega3.py',270),
  ('threat -> threat_description threat','threat',2,'p_threat','TP2_entrega3.py',271),
  ('threat -> threat_vulnerabilities threat','threat',2,'p_threat','TP2_entrega3.py',272),
  ('threat -> THREAT_CLOSE','threat',1,'p_threat','TP2_entrega3.py',273),
  ('threat_name -> THREAT_NAME_OPEN str THREAT_NAME_CLOSE','threat_name',3,'p_threat_name','TP2_entrega3.py',278),
  ('threat_description -> THREAT_DESCRIPTION_OPEN str THREAT_DESCRIPTION_CLOSE','threat_description',3,'p_threat_description','TP2_entrega3.py',283),
  ('threat_vulnerabilities -> THREAT_VULNERABILITIES_OPEN threat_vulnerabilities','threat_vulnerabilities',2,'p_threat_vulnerabilities','TP2_entrega3.py',288),
  ('threat_vulnerabilities -> threat_vulnerability threat_vulnerabilities','threat_vulnerabilities',2,'p_threat_vulnerabilities','TP2_entrega3.py',289),
  ('threat_vulnerabilities -> THREAT_VULNERABILITIES_CLOSE','threat_vulnerabilities',1,'p_threat_vulnerabilities','TP2_entrega3.py',290),
  ('threat_vulnerability -> VULNERABILITIES_VULNERABILITY_OPEN str VULNERABILITIES_VULNERABILITY_CLOSE','threat_vulnerability',3,'p_threat_vulnerability','TP2_entrega3.py',295),
  ('structure_security_policies -> SECURITY_POLICIES_OPEN security_policies SECURITY_POLICIES_CLOSE','structure_security_policies',3,'p_structure_security_policies','TP2_entrega3.py',306),
  ('security_policies -> security_policies security_policies','security_policies',2,'p_security_policies','TP2_entrega3.py',313),
  ('security_policies -> security_policy','security_policies',1,'p_security_policies','TP2_entrega3.py',314),
  ('security_policy -> SECURITY_POLICY_OPEN ID GENERAL_CLOSE POLICY_NAME_OPEN STRING POLICY_NAME_CLOSE POLICY_DESCRIPTION_OPEN STRING POLICY_DESCRIPTION_CLOSE security_objectives_SP additional_info_SP SECURITY_POLICY_CLOSE','security_policy',12,'p_security_policy','TP2_entrega3.py',321),
  ('security_objectives_SP -> SP_OBJECTIVES_OPEN SECURITY_OBJECTIVE_OPEN STRING SECURITY_OBJECTIVE_CLOSE SP_OBJECTIVES_CLOSE','security_objectives_SP',5,'p_security_objectives_SP','TP2_entrega3.py',329),
  ('additional_info_SP -> SP_ADDITIONAL_INFORMATION_OPEN SP_COMMENT_OPEN SP_COMMENT_CLOSE SP_ADDITIONAL_INFORMATION_CLOSE','additional_info_SP',4,'p_additional_info_SP','TP2_entrega3.py',336),
  ('structure_security_relationships -> SECURITY_RELATIONSHIP_OPEN security-relationships SECURITY_RELATIONSHIP_CLOSE','structure_security_relationships',3,'p_structure_security_relationships','TP2_entrega3.py',347),
  ('security-relationships -> security-relationships security-relationships','security-relationships',2,'p_security_relationships','TP2_entrega3.py',354),
  ('security-relationships -> LINKED_NODE_OPEN ID GENERAL_CLOSE linked-node LINKED_NODE_CLOSE','security-relationships',5,'p_security_relationships','TP2_entrega3.py',355),
  ('linked-node -> linked-node linked-node','linked-node',2,'p_expression_linked_node','TP2_entrega3.py',362),
  ('linked-node -> RELATIONSHIP_TYPE_OPEN ID GENERAL_CLOSE relationship-type RELATIONSHIP_TYPE_CLOSE','linked-node',5,'p_expression_linked_node','TP2_entrega3.py',363),
  ('relationship-type -> SECURITY_OBJECTIVES_OPEN security-objectives_SR SECURITY_OBJECTIVES_CLOSE','relationship-type',3,'p_expression_relationship_type','TP2_entrega3.py',371),
  ('security-objectives_SR -> security-objectives_SR security-objectives_SR','security-objectives_SR',2,'p_expression_security_objectives_SR','TP2_entrega3.py',379),
  ('security-objectives_SR -> SECURITY_OBJECTIVE_OPEN security-objective_SR security-objective_SR SECURITY_OBJECTIVE_CLOSE','security-objectives_SR',4,'p_expression_security_objectives_SR','TP2_entrega3.py',380),
  ('security-objective_SR -> SELF_OBJECTIVE_OPEN SELF_OBJECTIVE_CLOSE','security-objective_SR',2,'p_expression_security_objective_SR','TP2_entrega3.py',387),
  ('security-objective_SR -> PEER_OBJECTIVE_OPEN PEER_OBJECTIVE_CLOSE','security-objective_SR',2,'p_expression_security_objective_SR','TP2_entrega3.py',388),
  ('doc_comment -> COMMENT_OPEN doc_comment','doc_comment',2,'p_doc_comment','TP2_entrega3.py',403),
  ('doc_comment -> str doc_comment','doc_comment',2,'p_doc_comment','TP2_entrega3.py',404),
  ('doc_comment -> GENERAL_CLOSE','doc_comment',1,'p_doc_comment','TP2_entrega3.py',405),
  ('str -> STRING str','str',2,'p_string','TP2_entrega3.py',409),
  ('str -> STRING','str',1,'p_string','TP2_entrega3.py',410),
  ('str -> <empty>','str',0,'p_string','TP2_entrega3.py',411),
]