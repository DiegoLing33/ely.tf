"""
The HDO data navigator
"""
import core.hdo.consts as consts


class _HDONavigator:
    """
    The HDO Navigator
    """

    hdo = None
    """
    The HDO object
    :type HDO
    """

    def get_path(self) -> str:
        """
        Returns the path to the object directory
        :return: - the path
        """
        pass

    def get_dataset_path(self) -> str:
        """
        Returns the path to the dataset directory
        :return: - the path
        """
        pass

    def get_w2v_path(self) -> str:
        """
        Returns the path to w2v files directory
        :return: - the path
        """
        pass

    def get_s2s_path(self) -> str:
        """
        Returns the path to s2s files directory
        :return: - the path
        """
        pass

    def get_models_path(self) -> str:
        """
        Returns the path to models files directory
        :return: - the path
        """
        pass

    def get_file_path(self, dir_name: str, file: str) -> str:
        """
        Returns the full path to file in directory
        :param dir_name: - the directory const
        :param file: - the file const
        :return: - the path
        """
        pass

    def get_word_list_file_path(self) -> str:
        """
        Returns the path to the word list file
        :return:  - the path
        """
        pass

    def get_dataset_file_path(self, is_dict=False) -> str:
        """
        Returns the path to dataset file
        :param is_dict: - if sets True, returns the npy file with dictionary
        :return: - the path
        """
        pass

    def get_w2v_file_path(self, dim: str = ''):
        """
        Returns the w2v vector path or dictionary with paths
        :param dim: - if sets 'x', returns the path to x dimension vector file,
                      if sets 'y', returns the path to y dimension vector file,
                      else returns the dictionary dict(x = , y =)
        :return:
        """
        pass

    def get_s2s_file_path(self, dim: str = ''):
        """
        Returns the s2s vector path or dictionary with paths
        :param dim: - if sets 'x', returns the path to x dimension vector file,
                      if sets 'y', returns the path to y dimension vector file,
                      else returns the dictionary dict(x = , y =)
        :return:
        """
        pass


class HDONavigator(_HDONavigator):
    """
    The HDO Navigator
    """

    def get_path(self):
        return self.hdo.path

    def get_dataset_path(self):
        return self.get_path() + '/' + consts.HDO_DIR_DST

    def get_w2v_path(self):
        return self.get_path() + '/' + consts.HDO_DIR_W2V

    def get_s2s_path(self):
        return self.get_path() + '/' + consts.HDO_DIR_S2S

    def get_models_path(self):
        return self.get_path() + '/' + consts.HDO_DIR_MODELS

    def get_file_path(self, dir_name: str, file: str):
        return self.get_path() + '/' + dir_name + '/' + file

    def get_dataset_file_path(self, is_dict=False):
        return self.get_file_path(consts.HDO_DIR_DST, consts.HDO_FILE_CNV_DICT) if is_dict \
            else self.get_file_path(consts.HDO_DIR_DST, consts.HDO_FILE_CNV_DATA)

    def get_word_list_file_path(self):
        return self.get_file_path(consts.HDO_DIR_SOURCE, consts.HDO_FILE_WORLD_LIST)

    def get_w2v_file_path(self, dim: str = ''):
        if dim == consts.DIM_X:
            return self.get_file_path(consts.HDO_DIR_W2V, consts.HDO_FILE_W2V_X)
        elif dim == consts.DIM_Y:
            return self.get_file_path(consts.HDO_DIR_W2V, consts.HDO_FILE_W2V_Y)
        else:
            return dict(x=self.get_w2v_file_path(consts.DIM_X), y=self.get_w2v_file_path(consts.DIM_Y))

    def get_s2s_file_path(self, dim: str = ''):
        if dim == consts.DIM_X:
            return self.get_file_path(consts.HDO_DIR_S2S, consts.HDO_FILE_S2S_X)
        elif dim == consts.DIM_Y:
            return self.get_file_path(consts.HDO_DIR_S2S, consts.HDO_FILE_S2S_Y)
        else:
            return dict(x=self.get_s2s_file_path(consts.DIM_X), y=self.get_s2s_file_path(consts.DIM_Y))
