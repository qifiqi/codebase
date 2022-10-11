/* <h2>柱形图-就业行业</h2> */
(function () {
    // 初始化图标,这个是通过class定位
    var myChart = echarts.init(
        document.querySelector('.bar .chart'));
    // 通过json类型字典来进行设置参数
    var option;
    option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
                // 有shadow,line
            }
        },
        color: ["#2f89cf"],
        grid: {
            left: '0%',
            top: ".125rem",
            right: '0%',
            bottom: '4%',
            containLabel: true
        },
        xAxis: [
            {
                type: 'category',
                data: ["旅游行业", "教育培训", "游戏行业", "医疗行业", "电商行业", "社交行业", "金融行业"],
                axisTick: {
                    alignWithLabel: true
                },
                //  设置x轴的样式
                axisLabel: {
                    color: "rgba(255,255,255,.6)",
                    fontSize: 9,
                },
                // 设置x轴线不显示
                axisLine: {
                    show: false
                },
            }
        ],
        yAxis: [
            {
                type: 'value',
                // 设置轴样式
                axisLabel: {
                    color: "rgba(255,255,255,.6)",
                    fontSize: 12,
                },
                // 设置y轴线不显示
                axisLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,.1)",
                        width: 1,
                        type: "solid",
                    }
                },
                // 设置分割线
                splitLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,.1)"
                    }
                }
            }
        ],
        series: [
            {
                name: '直接访问',
                type: 'bar',
                barWidth: '35%',
                data: [200, 300, 300, 900, 1500, 1200, 600],
                // 修改柱子圆角
                itemStyle: {
                    barBorderRadius: 5
                }
            }
        ]
    };
    // 最后还要吧参数提交到图表
    myChart.setOption(option);
    //让我们的图表跟随屏幕自适应
    window.addEventListener('resize', function () {
        myChart.resize();
    })

})();

/* <h2>柱形图-技能掌握</h2> */
(function () {
    // 初始化图标,这个是通过class定位
    var myChart = echarts.init(
        document.querySelector('.bar2 .chart'));
    // 通过json类型字典来进行设置参数
    var mycol = ["#1089E7", "#F57474", "#56D0E3", "#F8B448", "#8B78F6"];
    var option;
    option = {
        grid: {
            left: '22%',
            top: "10%",
            bottom: '10%',
        },
        xAxis: {
            show: false,
        },
        yAxis: [
            {
                type: 'category',
                inverse: true,
                data: ["HTML5", "CSS3", "javascript", "VUE", "NODE"],
                //不显示线条
                axisLine: {
                    show: false,
                },
                // 不显示刻度
                axisTick: {
                    show: false,
                },
                axisLabel: {
                    color: "#fff",
                }

            },
            {
                show: true,
                inverse: true,
                data: [702, 350, 610, 793, 664],
                //不显示线条
                axisLine: {
                    show: false,
                },
                // 不显示刻度
                axisTick: {
                    show: false,
                },
                axisLabel: {
                    textStyle: {
                        fontSize: 12,
                        color: "#fff"
                    }
                },

            },
        ],
        series: [
            {
                name: '条',
                type: 'bar',
                yAxisIndex: 0,
                data: [70, 34, 60, 78, 69],
                // 柱子之间的距离
                barCategoryGap: 50,
                //柱子的宽度
                barWidth: 10,
                itemStyle: {
                    barBorderRadius: 20,
                    color: function (params) {
                        // console.log(params);
                        // 传进来的是一个对象
                        return mycol[params.dataIndex]
                    }
                },
                // 图形上的文本标签
                label: {
                    normal: {
                        show: true,
                        // 图形内显示
                        position: "inside",
                        // 文字的显示格式
                        formatter: "{c}%",
                        /**
                        标签内容格式器，支持字符串模板和回调函数两种形式，字符串模板与回调函数返回的字符串均支持用 \n 换行。
                        字符串模板 模板变量有：
                        {a}：系列名。
                        {b}：数据名。
                        {c}：数据值。
                         */
                    }
                },

            },
            {
                name: '框',
                type: 'bar',
                yAxisIndex: 1,
                data: [100, 100, 100, 100, 100],
                // 柱子之间的距离
                barCategoryGap: 50,
                //柱子的宽度
                barWidth: 15,
                itemStyle: {
                    barBorderRadius: 15,
                    color: "none",
                    borderWidth: 3,
                    borderColor: "#00c1de",
                },
            },
        ],
    };


    // 最后还要吧参数提交到图表
    myChart.setOption(option);
    //让我们的图表跟随屏幕自适应
    window.addEventListener('resize', function () {
        myChart.resize();
    })

})();

/* <h2>折线图-人员变化</h2> */
(function () {
    var yearData = [
        {
            year: '2020',  // 年份
            data: [  // 两个数组是因为有两条线
                [24, 40, 101, 134, 90, 230, 210, 230, 120, 230, 210, 120],
                [40, 64, 191, 324, 290, 330, 310, 213, 180, 200, 180, 79]
            ]
        },
        {
            year: '2021',  // 年份
            data: [  // 两个数组是因为有两条线
                [123, 175, 112, 197, 121, 67, 98, 21, 43, 64, 76, 38],
                [143, 131, 165, 123, 178, 21, 82, 64, 43, 60, 19, 34]
            ]
        }
    ];
    // 初始化图标,这个是通过class定位
    var myChart = echarts.init(
        document.querySelector('.line .chart'));
    // 通过json类型字典来进行设置参数
    var option;
    option = {
        color: ['#00f2f1', '#ed3f35'],
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: ['新增粉丝', '新增游客'],
            textStyle: {
                color: '#4c9bfd',
            },
            right: "10%",
        },
        grid: {
            top: "20%",
            left: '3%',
            right: '4%',
            bottom: '3%',
            show: true,//显示边框
            borderColor: '#012f4a',//设置边框颜色
            containLabel: true
        },
        xAxis: {
            type: 'category',
            data: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
            axisTick: {
                show: false // 去除刻度线
            },
            axisLabel: {
                fontSize: 10,
                color: '#4c9bfd' // 文本颜色
            },
            axisLine: {
                show: false // 去除轴线
            },
            boundaryGap: false  // 去除轴内间距
        },
        yAxis: {
            type: 'value',
            axisTick: {
                show: false,//取出刻度
            },
            axisLabel: {
                color: "#4c9bfd",//文字颜色
            },
            axisLine: {
                show: false,//取消轴线
            },
            splitLine: {
                lineStyle: {
                    color: "#012f4a",//分割线颜色
                }
            },
        },
        // 图标数据
        series: [
            {
                name: '新增粉丝',
                data: yearData[0].data[0],
                type: 'line',
                smooth: true //设置线条圆滑
            },
            {
                name: '新增游客',
                data: yearData[0].data[1],
                type: 'line',
                smooth: true
            }
        ]
    };

    // 最后还要吧参数提交到图表
    myChart.setOption(option);
    //让我们的图表跟随屏幕自适应
    window.addEventListener('resize', function () {
        myChart.resize();
    });
    $('.line h2').on("click", "a", function () {
        // 点击之后根据a的索引号来找
        // console.log($(this).index());
        // console.log(yearData[$(this).index()]);
        var datas_obj = yearData[$(this).index()]
        option.series[0].data = datas_obj.data[0]
        option.series[1].data = datas_obj.data[1]
        // 数据变化以后需要重新渲染
        myChart.setOption(option);

    });

})();

/* <h2>折线图-播放量</h2> */
(function () {
    var myChart = echarts.init(
        document.querySelector(".line2 .chart")
    )
    var option;
    option = {
        tooltip: {
            trigger: 'axis',
        },
        legend: {
            top: "0%",
            data: ['播放量', '转发量'],
            textStyle: {
                color: "rgba(255,255,255,.5)",
                fontSize: 12
            }
        },
        grid: {
            top: 30,
            left: 10,
            right: 10,
            bottom: 10,
            containLabel: true
        },
        xAxis: [
            {
                type: 'category',
                boundaryGap: false,
                data: ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "26", "28", "29", "30"],
                axisLabel: {
                    color: "rgba(255,255,255,.6)",
                    fontSize: 10,
                },
                axisLine: {
                    color: "rgba(255,255,255,.2)",
                },
            }
        ],
        yAxis: [
            {
                type: 'value',
                axisTick: {
                    show: false,
                },
                axisLabel: {
                    color: "rgba(255,255,255,.6)",
                    fontSize: 12,
                },
                axisLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,.1)",
                    },
                },
                splitLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,.1)",
                    }
                },
            }
        ],
        series: [
            {
                name: '播放量',
                type: 'line',
                smooth: true,//设置线条圆滑
                stack: 'Total',
                lineStyle: {
                    color: "#0184d5",
                    width: 2
                },
                emphasis: {
                    focus: 'series'
                },
                //设置填充
                areaStyle: {
                    color: new echarts.graphic.LinearGradient(
                        0,
                        0,
                        0,
                        1,
                        [
                            //设置起始颜色
                            {
                                offset: 0,
                                color: "rgba(1, 132, 213, 0.4)",
                            },
                            //设置结束颜色
                            {
                                offset: 0.8,
                                color: "rgba(1, 132, 213, 0.1)",
                            }
                        ],
                        false
                    ),
                    shadowColor: "rgba(0, 0, 0, 0.1)"
                },
                // 设置拐点 
                Symbol: "circle",
                // 拐点大小
                symbolSize: 5,
                // 设置在没有动作时不显示
                showSymbol: false,
                // 设置拐点样式
                itemStyle: {
                    color: "#0184d5",
                    borderColor: "rgba(221,220,107,.1)",
                    borderWidth: 10,
                },
                data: [30, 40, 30, 40, 30, 40, 30, 60, 20, 40, 30, 40, 30, 40, 30, 40, 30, 60, 20, 40, 30, 40, 30, 40, 30, 40, 20, 60, 50, 40],
            },
            {
                name: "转发量",
                type: "line",
                smooth: true,
                lineStyle: {
                    normal: {
                        color: "#00d887",
                        width: 2
                    }
                },
                areaStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(
                            0,
                            0,
                            0,
                            1,
                            [
                                {
                                    offset: 0,
                                    color: "rgba(0, 216, 135, 0.4)"
                                },
                                {
                                    offset: 0.8,
                                    color: "rgba(0, 216, 135, 0.1)"
                                }
                            ],
                            false
                        ),
                        shadowColor: "rgba(0, 0, 0, 0.1)"
                    }
                },
                // 设置拐点 小圆点
                symbol: "circle",
                // 拐点大小
                symbolSize: 5,
                // 设置拐点颜色以及边框
                itemStyle: {
                    color: "#00d887",
                    borderColor: "rgba(221, 220, 107, .1)",
                    borderWidth: 10
                },
                // 开始不显示拐点， 鼠标经过显示
                showSymbol: false,
                data: [130, 10, 20, 40, 30, 40, 80, 60, 20, 40, 90, 40, 20, 140, 30, 40, 130, 20, 20, 40, 80, 70, 30, 40, 30, 120, 20, 99, 50, 20],
            },


        ]
    };
    // 渲染
    myChart.setOption(option)
    window.addEventListener('resize', function () {
        myChart.resize();
    });
})();

/*<h2>饼状图-年龄发布</h2> */
(function () {
    var myChart = echarts.init(
        document.querySelector(".pie .chart")
    )
    var option;
    option = {
        color: [
            "#065aab",
            "#066eab",
            "#0682ab",
            "#0696ab",
            "#06a0ab",
        ],
        tooltip: {
            trigger: 'item'
        },
        legend: {
            bottom: "0%",
            // 修改图例小图标的大小
            itemWidth: 10,
            itemHeight: 10,
            textStyle: {
                color: "rgba(255,255,255,.5)",
                fontSize: 10,
            }
        },
        series: [
            {
                name: '年龄分布',
                type: 'pie',
                // 改动大小内半径，外半径
                radius: ['40%', '60%'],
                // 设置饼形图在容器中的位置
                center: ["50%", "45%"],
                avoidLabelOverlap: false,
                // 设置样式
                itemStyle: {
                    // 设置边框 
                    borderRadius: 10,
                    borderColor: '#00c1de',
                    // 设置线条宽度
                    borderWidth: 2,
                    // 设置透明度
                    opacity: 0.7,
                    // 阴影颜色
                    shadowColor: 'rgba(0,193,222, 0.5)',
                    // 阴影扩散的范围
                    shadowBlur: 10,
                },
                // 图像上的文字
                label: {
                    show: false,
                    position: 'center'
                },
                // 图像上文字的图像之间链接起来的线条
                labelLine: {
                    show: false
                },

                data: [
                    { value: 1, name: "0岁以下" },
                    { value: 4, name: "20-29岁" },
                    { value: 2, name: "30-39岁" },
                    { value: 2, name: "40-49岁" },
                    { value: 1, name: "50岁以上" }
                ],
            }
        ]
    };
    // 渲染
    myChart.setOption(option)
    window.addEventListener('resize', function () {
        myChart.resize();
    });
})();

/* <h2>饼状图-地区发布</h2> */
(function () {
    var myChart = echarts.init(
        document.querySelector(".pie2 .chart")
    )
    var option;
    option = {
        color: ['#006cff', '#60cda0', '#ed8884', '#ff9f7f', '#0096ff', '#9fe6b8', '#32c5e9', '#1d9dff'],
        tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        legend: {
            show: true,
            left: 'center',
            bottom: "0%",
            // 修改图例小图标的大小
            itemWidth: 10,
            itemHeight: 10,
            textStyle: {
                color: "rgba(255,255,255,.5)",
                fontSize: 10,
            }
        },
        series: [
            {
                name: 'Area Mode',
                type: 'pie',
                radius: ["10%", "70%"],
                center: ['50%', '45%'],
                // roseType: 'area',
                roseType: "radius",
                label: {
                    fontSize: 10,
                },
                // 设置链接线
                labelLine: {
                    show: true,
                    showAbove: true,
                    // 设置线条平滑度
                    smooth: 0.2,
                    // 链接文字
                    length: 6,
                    //链接到图像的
                    length2: 8,
                },
                itemStyle: {
                    // 设置边框 
                    borderRadius: 10,
                    // borderColor: '#00c1de',
                    // 设置线条宽度
                    borderWidth: 2,
                    // 设置透明度
                    opacity: 0.7,
                    // 阴影颜色
                    shadowColor: 'rgba(0,193,222, 0.2)',
                    // 阴影扩散的范围
                    shadowBlur: 10,
                },
                data: [
                    { value: 20, name: '云南' },
                    { value: 26, name: '北京' },
                    { value: 24, name: '山东' },
                    { value: 25, name: '河北' },
                    { value: 20, name: '江苏' },
                    { value: 25, name: '浙江' },
                    { value: 30, name: '四川' },
                    { value: 42, name: '湖北' }
                ]
            }
        ]
    };
    // 渲染
    myChart.setOption(option)
    window.addEventListener('resize', function () {
        myChart.resize();
    });
})();

