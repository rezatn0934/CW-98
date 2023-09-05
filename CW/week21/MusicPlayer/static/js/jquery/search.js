$(document).ready(function() {
  const searchBtn = $(".search-btn");
  const searchBox = $(".search-box");
  const searchInput = searchBox.find(".input");

  searchBtn.on("click", function() {
    searchBox.toggleClass("active");
    searchBtn.toggleClass("active");
    const searchIcon = searchBtn.find(".bi-search");
    const clockIcon = searchBtn.find(".bi-x-lg");

    if (searchInput.attr("type") == "hidden") {
      searchInput.attr("type", "search");
    } else {
      searchInput.attr("type", "hidden");
    }
    searchIcon.toggleClass("d-none");
    clockIcon.toggleClass("d-none");
  });
});