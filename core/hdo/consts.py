"""
Path consts file
"""

HDO_TEXT_FILES_FORMAT = '.hdtf'
HDO_NPY_FILES_FORMAT = '.hdnf'

# ------------------ Files ------------------

HDO_FILE_CNV_DATA = 'cnv' + HDO_TEXT_FILES_FORMAT
""" Conversation data text file name """

HDO_FILE_CNV_DICT = 'cnv' + HDO_NPY_FILES_FORMAT
""" Conversation dictionary npy file name """

HDO_FILE_WORLD_LIST = 'word-list' + HDO_TEXT_FILES_FORMAT
""" Word list text file name """

HDO_FILE_EMBED = 'emb-mtx' + HDO_NPY_FILES_FORMAT
""" Embedding matrix file npy name """

HDO_FILE_W2V_X = 'w2v-x' + HDO_NPY_FILES_FORMAT
""" W2V vector X npy file name """
HDO_FILE_W2V_Y = 'w2v-y' + HDO_NPY_FILES_FORMAT
""" W2V vector Y npy file name """

HDO_FILE_S2S_X = 's2s-x' + HDO_NPY_FILES_FORMAT
""" S2S vector x npy file name """
HDO_FILE_S2S_Y = 's2s-y' + HDO_NPY_FILES_FORMAT
""" S2S vector y npy file name """

HDO_FILE_LEARN = 'learn' + HDO_TEXT_FILES_FORMAT
""" HDO learn file name """

HDO_FILE_META = 'hdo' + HDO_TEXT_FILES_FORMAT
""" HDO meta file name """

# ------------------ Directories ------------------

HDO_DIR_DST = 'dataset'
""" Dataset directory name """
HDO_DIR_W2V = 'w2v'
""" W2V vectors directory name """
HDO_DIR_S2S = 's2s'
""" S2S vectors directory name """
HDO_DIR_MODELS = 'models'
""" S2S vectors directory name """
HDO_DIR_SOURCE = 'source'
""" Source directory name """

# ------------------ Core consts ------------------

DIM_X = 'x'
""" The x dimension """
DIM_Y = 'y'
""" The y dimension """
