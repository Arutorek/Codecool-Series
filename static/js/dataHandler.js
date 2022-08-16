export let dataHandler = {
    getShowsByActors: async function (actorId) {
        const response = await apiGet(`/api/actor-shows/${actorId}/`);
        return response;
    },
    getCharacters: async function (characterId) {
        const response = await apiGet(`/api/get-characters/${characterId}`);
        return response;
    }
}

async function apiGet(url) {
    let response = await fetch(url, {
        method: 'GET',
    });
    if (response.status === 200) {
        let data = await response.json()
        console.log(data)
        return data;
    }
}

async function apiPost(url, payload, ) {
  let response = await fetch(url, {
    method: "POST",
    body: JSON.stringify({
      payload
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
  })
  if (response.status === 200) {
    let data = response.json();
    console.log(data)
    return data;
  }
}