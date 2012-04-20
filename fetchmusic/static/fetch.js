var hideAllReleases = function() {
    elements = document.getElementsByClassName("release-selected")
    for(i = 0; i < elements.length; i++){
        elements[i].classList.remove("release-selected");
    }
}

var handleReleaseClick = function(e) {
    e.preventDefault();
    section = this.parentElement.parentElement
    if(section.classList.contains("release-selected")) {
        section.classList.remove("release-selected");
    }
    else {
        hideAllReleases();
        section.classList.add("release-selected");
    }
    console.log(this.id);
}

var injectOnClicks = function(){
    releases = document.getElementsByClassName("release-title");
    for(i = 0; i < releases.length; i++) {
        releases[i].onclick=handleReleaseClick;
    }
}

var handleFetch = function(e) {
    e.preventDefault();
    formdat = {tracker_name: this.dataset.name, tracker_id: this.dataset.id}
    $.post('itemfetch', formdat,
           function(data) {
               console.log(data)
           })
}
var makeFetchReactive = function() {
    fetches = document.getElementsByClassName("btn-fetch");
    for (i = 0; i < fetches.length; i++) {
        fetches[i].onclick = handleFetch;
    }
}

window.onload = function()
{
    injectOnClicks();
    makeFetchReactive();
}