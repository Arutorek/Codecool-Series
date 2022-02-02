import {dataHandler} from "./dataHandler.js";


window.onload = function () {
    addListeners()
}


function addListeners() {
    document.querySelectorAll('.actors').forEach(actors => {
        actors.addEventListener('click', createTableForShow)
    })
}


async function createTableForShow(clickEvent) {
    let shows = await getShows(clickEvent)
    if (!clickEvent.target.querySelector("#shows-table")) {
        deleteTable()
        createTable(shows, clickEvent)
    } else {
        deleteTable()
    }
}


function createTable(shows, clickEvent) {
    var showsTable = document.createElement("TABLE")
    showsTable.setAttribute("id", "shows-table")
    for (let show of shows) {
        let createRow = showsTable.insertRow()
        createRow.insertCell().innerHTML = `${show['title']}`
    }
    clickEvent.target.appendChild(showsTable)
}


function deleteTable() {
    if (document.getElementById("shows-table")) {
        document.getElementById("shows-table").remove()
    }
}


async function getShows(clickEvent) {
    let actorId = clickEvent.target.dataset.id
    return await dataHandler.getShowsByActors(actorId)
}

