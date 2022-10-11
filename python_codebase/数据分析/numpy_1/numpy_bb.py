# coding =utf-8
import numpy as np


def fill_ndarray(t1):
    for i in range(t1.shape[1]):
        temp_col = t1[:, i]  # 获取当前列
        print(temp_col)
        num_zero = np.count_nonzero(temp_col != temp_col)
        if num_zero != 0:  # 不为0这说明当前这一列中有nan
            temp_not_nan_cl = temp_col[temp_col == temp_col]
            # 选中当前为nan的值，把均值传进去，替换掉
            temp_col[np.isnan(temp_col)] = temp_not_nan_cl.mean()
    return t1


if __name__ == '__main__':
    t1 = np.arange(24).reshape((4, 6)).astype('float')
    t1[1, 2:] = np.nan
    print(t1 != t1)

    fill_ndarray(t1)
    # print(np.nan != np.nan)

    print(t1)
