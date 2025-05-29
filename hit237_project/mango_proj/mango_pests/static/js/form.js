const step1 = document.getElementById("form-step-1");
    const step2 = document.getElementById("form-step-2");
    const step3 = document.getElementById("form-step-3");

    document.getElementById("nextToStep2").addEventListener("click", function () {
        step1.style.display = "none"; step2.style.display = "block";});

    document.getElementById("backToStep1").addEventListener("click", function () {
        step2.style.display = "none";step1.style.display = "block";});

    document.getElementById("nextToStep3").addEventListener("click", function () {
        step2.style.display = "none";
        step3.style.display = "block";
    });

    document.getElementById("backToStep2").addEventListener("click", function () {
        step3.style.display = "none";
        step2.style.display = "block";
    });