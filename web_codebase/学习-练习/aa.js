// ==UserScript==
// @name         考试宝
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  没有准确率要注意，谨慎使用
// @author       小符
// @match        https://www.zaixiankaoshi.com/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=zaixiankaoshi.com
// @require      https://cdn.bootcdn.net/ajax/libs/jquery/3.6.0/jquery.js
// ==/UserScript==

//生成从minNum到maxNum的随机数
function randomNum(minNum, maxNum) {
    switch (arguments.length) {
        case 1:
            return parseInt(Math.random() * minNum + 1, 10);
            break;
        case 2:
            return parseInt(Math.random() * (maxNum - minNum + 1) + minNum, 10);
            break;
        default:
            return 0;
            break;
    }
}

(function () {
    'use strict';
    $(() => {
        console.log('ok')

        let setI = setInterval(() => {
            const btnJEle = $('.el-button--primary')
            const clsEle = $('.is-disabled:contains(下一题)')
            if (clsEle.length > 0) {
                clearInterval(setI);
                $('.submit-btn').click();
            } else {
                const divOptJle = $('.option')
                const btnP = $('.opcity-btn')
                const tjEle = $('button:contains(提交答案)');
                const paixEle = $('.paixu')


                if (divOptJle.length > 0) {
                    if (paixEle.length > 0) {
                        for (let i = 0; i < divOptJle.length; i++) {
                            divOptJle[i].click();
                        }
                        tjEle.click();
                    } else {
                        if (tjEle.length>0){
                            for (let i = 0; i < divOptJle.length; i++) {
                                divOptJle[i].click();
                            }
                            tjEle.click();
                        }
                        for (let i = 0; i < divOptJle.length; i++) {
                            if (divOptJle[i].classList.contains('right')) {
                                divOptJle[i].classList.remove('right');
                            }
                        }
                        if (divOptJle.length < 4) {
                            const num = randomNum(0, 1)
                            divOptJle[num].click();
                        } else {
                            const num = randomNum(0, 3)
                            divOptJle[num].click();
                        }
                    }

                } else if (btnP.length > 0) {
                    $('.el-input__inner').text("sb")
                    btnP.click();
                }

                btnJEle.click();


            }
        }, 50)


    })
    // Your code here...
})();
