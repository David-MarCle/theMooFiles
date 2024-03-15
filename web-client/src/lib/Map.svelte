<script>
  // @ts-nocheck
  import iconMarker from "../assets/marker_icon.svg";
  import mapStyles from "./map-styles.js";
  import { onMount } from "svelte";

  let container;
  let map;
  let zoom = 9;
  let center = { lat: 43.75544, lng: -5.92225 };

  onMount(async () => {
    const endpoint = `http://localhost:8000/api/abductions/`;
    const response = await fetch(endpoint);
    const data = await response.json();

    map = new google.maps.Map(container, {
      zoom,
      center,
      styles: mapStyles,
    });
    console.log(data[0].photo)
    for (let i = 0; i < data.length; i++) {
      const marker = new google.maps.Marker({
        
        position: { lat: parseFloat(data[i].latitude), lng: parseFloat(data[i].longitude) },
        icon: iconMarker,
      });

      marker.setMap(map);

      marker.addListener("click", () => {
        let infowindow = new google.maps.InfoWindow({
          content: `<div style="display: flex; flex-direction: column; gap:.5rem; width: 200px;">
                      <h2>${data[i].name}<h2>
                      <h3>${data[i].place}</h3>
                      <p>${data[i].description}</p>
                      <img style="width: 200px; align-self: center;" src="${data[i].photo}">
                    </div>
                    `,
        });

        infowindow.open(map, marker);
      });
    }
  });
</script>

<div class="full-screen" bind:this={container}></div>

<style>
  .full-screen {
    width: 100vw;
    height: 100vh;
  }
</style>
