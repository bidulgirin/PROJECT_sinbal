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
    const count = document.querySelector("#count"); // 실제 form 에 사용할 값
    console.log(count);
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
        count.value = result;
    }

    decr.addEventListener("click", decrease);
    incr.addEventListener("click", increase);
});
