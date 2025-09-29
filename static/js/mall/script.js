document.addEventListener("DOMContentLoaded", function () {
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
    const cart = document.getElementById("cart");
    let result = 0; // 초기 숫자

    function decrease() {
        // 감소 result 가 0보다 클경우에만 -1 되시오
        if (result > 0) {
            let dec = (result -= 1);
        }
        num();
    }

    function increase() {
        // 증가
        let inc = (result += 1);
        num();
    }

    function num() {
        // 출력
        document.getElementById("print").innerHTML = result;
        quantity.value = result;
    }
    // 이벤트 리스너
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

    //

    // 장바구니 버튼을 눌렀을때
    let form = document.getElementById("form");
    const parchase = document.getElementById("parchase");

    // 장바구니를 클릭할경우
    cart.addEventListener("click", (e) => {
        e.preventDefault();
        // 유저가 로그인했는지 체크
        user_login_check();
        if (quantity.value == 0) {
            alert("수량을 선택해주세요");
            return false;
        }

        form.method = "POST";
        form.action = cart_add_url;
        form.submit();
    });
    // 구매하기 클릭한경우 : 결제하기기능동작
    parchase.addEventListener("click", (e) => {
        e.preventDefault();
        const size = Number(document.getElementById("size").value);
        const quantity_ = Number(document.getElementById("quantity").value);

        // 유저가 로그인했는지 체크
        user_login_check();

        if (quantity_ == 0) {
            alert("수량을 선택해주세요");
            return false;
        }

        form.method = "GET";
        form.action = `/mall/quick_parchase/?shoe_id=${shoe_id}&size=${size}&quantity=${quantity_}`;
        form.submit();
    });

    // 찜 ========================================================
    // 찜을 눌렀을때
    const wishBtn = document.getElementById("checkbox"); // 찜버튼
    function wishListSubmit() {
        const form = document.createElement("form");
        form.setAttribute("method", "GET"); //Post 방식

        if (wishBtn.checked) {
            // 위시리스트에서 빼는 작업
            form.setAttribute("action", mall_wishlist_add); //요청 보낼 주소
        } else {
            form.setAttribute("action", mall_wishlist_remove); //요청 보낼 주소
        }

        // 신발 아이디
        hiddenField = document.createElement("input");

        hiddenField.setAttribute("type", "hidden");
        hiddenField.setAttribute("name", "shoe_id");
        hiddenField.setAttribute("value", "{{data.id}}");
        form.appendChild(hiddenField);

        document.body.appendChild(form);
        form.submit();
    }

    wishBtn.addEventListener("click", wishListSubmit);
});
