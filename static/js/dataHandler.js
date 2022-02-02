export let dataHandler = {
    getShowsByActors: async function (actorId) {
        const response = await apiGet(`/api/actor-shows/${actorId}/`);
        return response;
    },
}


async function apiGet(url) {
    let response = await fetch(url, {
        method: 'GET',
    });
    if (response.status === 200) {
        let data = await response.json()
        return data;
    }
}