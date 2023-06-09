from pyecharts.charts import Bar
from pyecharts import options as opts
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType

# bar = Bar()
# bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# # render 会生成本地 HTML 文件，默认会在当前目录生成 地图.html 文件
# # 也可以传入路径参数，如 bar.render("mycharts.html")


bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("aa", [5, 20, 36, 10, 75, 90])
        .add_yaxis("bb", [15, 6, 45, 20, 35, 66])
        .set_global_opts(title_opts=opts.TitleOpts(title="买衣服", subtitle="不买"))
)
bar.render()
