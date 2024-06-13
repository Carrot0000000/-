# -*- coding:utf-8 -*-

import tensorflow as tf
import matplotlib as mpl

# 可以显示中文
mpl.rcParams['font.sans-serif'] = ['KaiTi']
mpl.rcParams['font.serif'] = ['KaiTi']

# 垃圾类名
class_names=['其他垃圾_PE塑料袋', '其他垃圾_一次性杯子', '其他垃圾_一次性棉签', '其他垃圾_口罩', '其他垃圾_唱片', '其他垃圾_干燥剂', '其他垃圾_打火机', '其他垃圾_搓澡巾', '其他垃圾_滚筒纸', '其他垃圾_点燃的香烟', '其他垃圾_眼镜', '其他垃圾_笔', '其他垃圾_胶带', '其他垃圾_验孕棒', '其他垃圾_鸡毛掸', '厨余垃圾_圣女果', '厨余垃圾_地瓜', '厨余垃圾_大蒜', '厨余垃圾_梨', '厨余垃圾_橙子', '厨余垃圾_火龙果', '厨余垃圾_瓜子壳', '厨余垃圾_番茄', '厨余垃圾_白菜叶', '厨余垃圾_苹果', '厨余垃圾_草莓', '厨余垃圾_菠萝', '厨余垃圾_菠萝蜜', '厨余垃圾_蘑菇', '厨余垃圾_蛋', '厨余垃圾_蛋挞', '厨余垃圾_蛋糕', '厨余垃圾_西瓜皮', '厨余垃圾_豆', '厨余垃圾_豆腐', '厨余垃圾_辣椒', '厨余垃圾_面包', '厨余垃圾_饼干', '厨余垃圾_香蕉皮', '可回收物_A4纸', '可回收物_一次性筷子', '可回收物_不锈钢管', '可回收物_乒乓球拍', '可回收物_书', '可回收物_保温杯', '可回收物_信封', '可回收物_充电头', '可回收物_充电宝', '可回收物_充电线', '可回收物_凳子', '可回收物_刀', '可回收物_剪刀', '可回收物_勺子叉子', '可回收物_包', '可回收物_卡', '可回收物_台灯', '可回收物_吹风机', '可回收物_呼啦圈', '可回收物_塑料瓶', '可回收物_塑料盆', '可回收物_头戴式耳机', '可回收物_尺子', '可回收物_布制品', '可回收物_帽子', '可回收物_手机', '可回收物_手电筒', '可回收物_手表', '可回收物_打气筒', '可回收物_拉杆箱', '可回收物_插线板', '可回收物_收音机', '可回收物_放大镜', '可回收物_易拉罐', '可回收物_望远镜', '可回收物_木制切菜板', '可回收物_木质梳子', '可回收物_木质锅铲', '可回收物_枕头', '可回收物_桌子', '可回收物_水壶', '可回收物_水杯', '可回收物_泡沫板', '可回收物_灭火器', '可回收物_热水瓶', '可回收物_电动剃须刀', '可回收物_电子秤', '可回收物_电熨斗', '可回收物_电磁炉', '可回收物_电路板', '可回收物_电风扇', '可回收物_电饭煲', '可回收物_盘子', '可回收物_碗', '可回收物_箱子', '可回收物_纸板', '可回收物_衣架', '可回收物_袜子', '可回收物_裙子', '可回收物_裤子', '可回收物_计算器', '可回收物_订书机', '可回收物_话筒', '可回收物_路由器', '可回收物_轮胎', '可回收物_遥控器', '可回收物_钥匙', '可回收物_铁丝球', '可回收物_键盘', '可回收物_镊子', '可回收物_闹钟', '可回收物_雨伞', '可回收物_鞋', '可回收物_鼠标', '有害垃圾_太阳能电池', '有害垃圾_灯', '有害垃圾_电池', '有害垃圾_纽扣电池', '有害垃圾_胶水', '有害垃圾_药品包装', '有害垃圾_蓄电池']
print(len(class_names))

# 数据加载，按照8:2的比例加载垃圾数据
def data_load(data_dir, img_height, img_width, batch_size):
    test_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        label_mode='categorical',
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size)
    class_names = test_ds.class_names
    return test_ds,  class_names


# 测试mobilenet的准确率
def my_MobileNet():
    test_ds, class_names = data_load("F:/毕设_垃圾分类/总结综合/images/test", 224, 224, 8)
    print(class_names)
    model = tf.keras.models.load_model("F:/毕设_垃圾分类/总结综合/my_MobileNet/models/MobileNetV2_80layers_epoch30.h5")
    model.summary()
    loss, accuracy = model.evaluate(test_ds)
    print('my_MobileNet test accuracy :', accuracy)


if __name__ == '__main__':
    my_MobileNet()
