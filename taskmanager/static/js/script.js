document.addEventListener('DOMContentLoaded', function () {
    // sidenav initialiization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // datepicker
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
        format: "dd mmm, yy",
        i18n: { done: "Select" }
    });

    // selects
    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);

    // colapsibles
    let collapsibles = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsibles);
});
