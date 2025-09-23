document.addEventListener("DOMContentLoaded", function () {
    // 스플라이드 쓸 생각 있니? 없음~
    // 이미지가 여러장이면 쓸 의향있음
    // 크롤링 데이터를 생성할때 이미지가 1개만 불러올거기때문에 일단 이렇게 처리
    // const elms = document.getElementsByClassName("splide");

    // for (let i = 0; i < elms.length; i++) {
    //     new Splide(elms[i]).mount();
    // }

    // 탭기능 ==========================================
    const mainContent = document.querySelector("#tab_container");
    const tabs = document.querySelectorAll(".btn");
    const content = document.querySelectorAll(".content");

    //USING addEventListener and NORMAL FUNCTIONS
    mainContent.addEventListener("click", function (e) {
        //Listen to an element with a dataset with an ID
        const id = e.target.dataset.id;
        if (id) {
            tabs.forEach(function (tab) {
                tab.classList.remove("active");
            });

            e.target.classList.add("active");

            content.forEach(function (content) {
                content.classList.remove("active");
            });

            const activeTab = document.getElementById(id);
            activeTab.classList.add("active");
        }
    });

    // 개수===================================================

    const decr = document.querySelector("#decr"); // 감소버튼
    const incr = document.querySelector("#incr"); // 증가버튼
    const quantity = document.querySelector("#quantity"); // 실제 form 에 사용할 값

    let result = 0; // 초기 숫자
    function buttonState() {
        // 수량셈
        const quantity_val = Number(quantity.value);
        // cart 누르면
        cart.disable = quantity_val <= 0;
    }
    function decrease() {
        // 감소 result 가 0보다 클경우에만 -1 되시오
        if (result > 0) {
            let dec = (result -= 1);
        }
        num();
        buttonState();
    }

    function increase() {
        // 증가
        let inc = (result += 1);
        num();
        buttonState();
    }

    function num() {
        // 출력
        document.getElementById("print").innerHTML = result;
        quantity.value = result;
    }

    decr.addEventListener("click", decrease);
    incr.addEventListener("click", increase);

    // 이미지 썸네일
    const thumbs = $(".img-selection").find("img");

    thumbs.click(function () {
        var src = $(this).attr("src");
        var dp = $(".display-img");
        var img = $(".zoom");
        dp.attr("src", src);
        img.attr("src", src);
    });

    $(".img-thumbnail").click(function () {
        $(".img-thumbnail").removeClass("selected");
        $(this).addClass("selected");
    });

    const zoom = $(".big-img").find("img").attr("src");
    $(".big-img").append('<img class="zoom" src="' + zoom + '">');
    $(".big-img").mouseenter(function () {
        $(this).mousemove(function (event) {
            const offset = $(this).offset();
            const left = event.pageX - offset.left;
            const top = event.pageY - offset.top;

            $(this).find(".zoom").css({
                width: "200%",
                opacity: 1,
                left: -left,
                top: -top,
            });
        });
    });

    $(".big-img").mouseleave(function () {
        $(this).find(".zoom").css({
            width: "100%",
            opacity: 0,
            left: 0,
            top: 0,
        });
    });
});
