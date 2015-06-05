from struct import calcsize

from ryu.ofproto.ofproto_common import OFP_HEADER_SIZE
OFP_OXM_EXPERIMENTER_HEADER_SIZE = 8

#state ofp_exp_msg_state_mod
OFP_EXP_STATE_MOD_PACK_STR='!Bx'
OFP_EXP_STATE_MOD_SIZE =18
assert (calcsize(OFP_EXP_STATE_MOD_PACK_STR)) + OFP_HEADER_SIZE + OFP_OXM_EXPERIMENTER_HEADER_SIZE == OFP_EXP_STATE_MOD_SIZE

#struct ofp_exp_stateful_table_config
OFP_EXP_STATE_MOD_STATEFUL_TABLE_CONFIG_PACK_STR='!BB'
OFP_EXP_STATE_MOD_STATEFUL_TABLE_CONFIG_SIZE = 2
assert (calcsize(OFP_EXP_STATE_MOD_STATEFUL_TABLE_CONFIG_PACK_STR)== OFP_EXP_STATE_MOD_STATEFUL_TABLE_CONFIG_SIZE)

#struct ofp_exp_set_extractor
MAX_FIELD_COUNT=6
OFP_EXP_STATE_MOD_EXTRACTOR_PACK_STR='!B3xI'
OFP_EXP_STATE_MOD_EXTRACTOR_SIZE = 8
assert (calcsize(OFP_EXP_STATE_MOD_EXTRACTOR_PACK_STR) == OFP_EXP_STATE_MOD_EXTRACTOR_SIZE)

# struct ofp_exp_set_flow_state
MAX_KEY_LEN=48
OFP_EXP_STATE_MOD_SET_FLOW_STATE_PACK_STR='!B3xIII'
OFP_EXP_STATE_MOD_SET_FLOW_ENTRY_SIZE = 16
assert (calcsize(OFP_EXP_STATE_MOD_SET_FLOW_STATE_PACK_STR) == OFP_EXP_STATE_MOD_SET_FLOW_ENTRY_SIZE)

# struct ofp_exp_del_flow_state
OFP_EXP_STATE_MOD_DEL_FLOW_STATE_PACK_STR='!B3xI'
OFP_EXP_STATE_MOD_DEL_FLOW_ENTRY_SIZE = 8
assert (calcsize(OFP_EXP_STATE_MOD_DEL_FLOW_STATE_PACK_STR) == OFP_EXP_STATE_MOD_DEL_FLOW_ENTRY_SIZE)
 
#state ofp_exp_set_global_state
OFP_EXP_STATE_MOD_SET_GLOBAL_STATE_PACK_STR='!II'
OFP_EXP_STATE_MOD_SET_GLOBAL_ENTRY_SIZE = 8
assert (calcsize(OFP_EXP_STATE_MOD_SET_GLOBAL_STATE_PACK_STR)) == OFP_EXP_STATE_MOD_SET_GLOBAL_ENTRY_SIZE

#struct ofp_exp_action_set_state
OFP_EXP_ACTION_SET_STATE_PACK_STR = '!I4xIIB7x'
OFP_EXP_ACTION_SET_STATE_SIZE = 24
assert calcsize(OFP_EXP_ACTION_SET_STATE_PACK_STR) == OFP_EXP_ACTION_SET_STATE_SIZE

#struct ofp_exp_action_set_flag
OFP_EXP_ACTION_SET_FLAG_PACK_STR = '!I4xII'
OFP_EXP_ACTION_SET_FLAG_SIZE = 16
assert calcsize(OFP_EXP_ACTION_SET_FLAG_PACK_STR) == OFP_EXP_ACTION_SET_FLAG_SIZE

# struct ofp_state_stats_request
_OFP_STATE_STATS_REQUEST_0_PACK_STR = 'B7x'
OFP_STATE_STATS_REQUEST_0_PACK_STR = '!' + _OFP_STATE_STATS_REQUEST_0_PACK_STR
OFP_STATE_STATS_REQUEST_0_SIZE = 8
assert (calcsize(OFP_STATE_STATS_REQUEST_0_PACK_STR) ==
        OFP_STATE_STATS_REQUEST_0_SIZE)

# struct ofp_state_stats
_OFP_STATE_STATS_0_PACK_STR = 'HBxI'
OFP_STATE_STATS_0_PACK_STR = '!' + _OFP_STATE_STATS_0_PACK_STR
OFP_STATE_STATS_0_SIZE = 8
assert calcsize(OFP_STATE_STATS_0_PACK_STR) == OFP_STATE_STATS_0_SIZE

#enum ofp_exp_messages
OFPT_EXP_STATE_MOD = 0

#enum ofp_state_mod_command 
OFPSC_STATEFUL_TABLE_CONFIG = 0
OFPSC_EXP_SET_L_EXTRACTOR   = 1
OFPSC_EXP_SET_U_EXTRACTOR   = 2
OFPSC_EXP_SET_FLOW_STATE    = 3
OFPSC_EXP_DEL_FLOW_STATE    = 4
OFPSC_SET_GLOBAL_STATE      = 5
OFPSC_RESET_GLOBAL_STATE    = 6

#enum ofp_exp_actions
OFPAT_EXP_SET_STATE = 0
OFPAT_EXP_SET_FLAG  = 1

#enum ofp_stats_extension_commands
OFPMP_EXP_STATE_STATS = 0
OFPMP_EXP_FLAGS_STATS = 1