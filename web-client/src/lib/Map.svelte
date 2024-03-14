<script>
  // @ts-nocheck
  import iconMarker from "../assets/marker_icon.svg";
  import mapStyles from "./map-styles.js";

  let container;
  let map;
  let zoom = 8;
  let center = { lat: 43.363129, lng: -5.951843 };

  import { onMount } from "svelte";

  onMount(async () => {
    map = new google.maps.Map(container, {
      zoom,
      center,
      styles: mapStyles,
    });

    const marker = new google.maps.Marker({
      position: { lat: 43.363129, lng: -5.951843 },
      icon: iconMarker,
    });

    marker.setMap(map);

    marker.addListener("click", () => {
      let infowindow = new google.maps.InfoWindow({
        content: `Infomación de cada abducción`,
      });

      infowindow.open(map, marker);

    });

  });
</script>

<div class="full-screen" bind:this={container}></div>

<style>
  .full-screen {
    width: 100vw;
    height: 100vh;
  }
</style>
