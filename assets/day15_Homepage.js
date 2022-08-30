var books = [{
        id: 1,
        src: "{{url_for('static',filename='images/Inkognito.jpg')}}",
        bookName: "Inkognito",
        authorName: "David Eagleman",
        genre: "psixologiya"
    },
    {
        id: 2,
        src: "{{url_for('static',filename='images/1984_book.jpg')}}",
        bookName: "1984",
        authorName: "Corc Oruell",
        genre: "elmi-fantastik"
    },
    {
        id: 3,
        src: "{{url_for('static',filename='images/hamlet.jpg')}}",
        bookName: "Hamlet",
        authorName: "Uilyam Şekspir",
        genre: "roman"
    },
    {
        id: 4,
        src: "{{url_for('static',filename='images/Palto_book.jpg')}}",
        bookName: "Palto",
        authorName: "Nikolay Qoqol",
        genre: "roman"
    },
    {
        id: 5,
        src: "{{url_for('static',filename='images/otello.jpg')}}",
        bookName: "Otello",
        authorName: "Uilyam Şekspir",
        genre: "roman"
    },
    {
        id: 6,
        src: "{{url_for('static',filename='images/sefiller.jpg')}}",
        bookName: "Səfillər",
        authorName: "Viktor Hüqo",
        genre: "roman"
    }
]
let chosenBook = [];
let addBook;
let indexOfBook;
let numberOfBook = 0;
$("#plusSign").click(function () {
    $(".element-item").addClass("d-none");
    $(".others").removeClass("d-none");
    $container.addClass("d-none")
    $container.removeClass("d-flex");
    $container.removeClass("flex-wrap");
    $container.removeClass("position-static");
    condition = true;
    indexOfBook = Math.floor(Math.random() * books.length);
    while (condition) {
        if ((chosenBook.includes(indexOfBook)) && (chosenBook.length < 6)) {
            indexOfBook = Math.floor(Math.random() * books.length);
        } else if (chosenBook.length == 6) {
            condition = false;
        } else {
            numberOfBook++;
            $("#number").val(numberOfBook);
            chosenBook.push(indexOfBook);
            addBook =
                `
            <div class="col-4 mb-5 d-flex flex-column align-items-center others" id=${books[indexOfBook].id}>
                <div class="w-50 h-75">
                    <img src=${books[indexOfBook].src} class="card-img-top h-100" alt="...">
                </div>
                <div class="card-body border w-50">
                    <h2 class="card-title">${books[indexOfBook].bookName}</h2>
                    <p class="card-text">${books[indexOfBook].authorName}</p>
                    <a href="Product.html" class="btn text-light bg-info">Ətraflı</a>
                </div>
            </div>
            `
            $(".row").append(addBook);
            condition = false;
        }
    }
});
$("#minusSign").click(function () {
    if (numberOfBook != 0) {
        numberOfBook--;
        $(".element-item").addClass("d-none");
        $(".others").removeClass("d-none");
        $container.addClass("d-none")
        $container.removeClass("d-flex");
        $container.removeClass("flex-wrap");
        $container.removeClass("position-static");
        $("#number").val(numberOfBook);
        chosenBook.splice($.inArray(chosenBook, $(".row").children('.others:last')[0].id));
        $(".row").children(':last').detach();
    }
});
var $container = $('.grid');
$container.isotope({
    animationEngine: 'best-available',
    itemSelector: '.element-item'
});
$('#filters button').on('click', function () {
    var selector = $(this).data('filter');
    $(".others").addClass("d-none");
    $(".element-item").removeClass("d-none");
    $container.removeClass("d-none")
    $container.addClass("d-flex");
    $container.addClass("flex-wrap");
    $container.addClass("position-static");
    $container.addClass("h-100");
    $container.isotope({
        filter: selector,
    });
    $(".element-item").each(function (i) {
        $(".element-item")[i]["style"]["transform"] = "";
        if (selector === "*") {
            $(".element-item")[i].className = "col-4 mb-5 d-flex flex-column align-items-center element-item position-static";
        } else if ($(".element-item")[i].dataset.category != selector) {
            $(".element-item")[i].className = "col-4 mb-5 d-none flex-column align-items-center element-item position-static";

        } else if ($(".element-item")[i].dataset.category == selector) {
            $(".element-item")[i].className = "col-4 mb-5 d-flex flex-column align-items-center element-item position-static opacity-100";

        }
    });
});
$("#calculation").click(function () {
    if ($("#calculation").html() === "Başla") {
        $("#calculation").html("Bitir");
        $("#calculation").removeClass("btn-warning");
        $("#calculation").addClass("btn-danger");
        $("#calculationSide").append(
            `
            <div class="d-flex justify-content-between pb-5" id="hideSide">
                <input type="number" name="numberOfPage" id="numberOfPage" class="border rounded" style="width: 39%;">
                <input type="number" name="numberOfDay" id="numberOfDay" class="border rounded" style="width: 39%">
                <button type="button" name="calculate" class="btn text-light bg-info" id="calculate" style="width: 20%">Hesabla</button>
            </div>
            `
        );
        $("#calculate").click(function () {
            $("#infoAlert").remove();
            var numberOfPage = $("#numberOfPage").val();
            var numberOfDay = $("#numberOfDay").val();
            if (numberOfPage > 0 && numberOfDay > 0) {
                var result = Math.ceil(numberOfPage / numberOfDay);
                $("#calculationSide").prepend(
                    `
                    <div class="alert alert-success py-4 mb-5 text-center fs-5" role="alert" id="infoAlert">
                       Hər gün ən az səhifə <span id="page"></span> oxumalısınız!
                    </div>
                    `
                );
                $("#page").html(result).addClass("fs-3 fw-bold");
            } else {
                $("#calculationSide").prepend(
                    `
                    <div class="alert alert-danger py-4 mb-5 text-center fs-5" role="alert" id="infoAlert">
                        Hesablamada xəta baş verdi!
                    </div>
                    `
                );
            }
        });
    } else {
        $("#calculation").html("Başla");
        $("#calculation").removeClass("btn-danger");
        $("#calculation").addClass("btn-warning");
        $("#hideSide").remove();
        $("#infoAlert").remove();
    }
})