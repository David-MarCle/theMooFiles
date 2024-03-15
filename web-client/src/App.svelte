<script>
  import Header from "../src/lib/header/Header.svelte";
  import Footer from "./lib/footer/Footer.svelte";
  import Map from "./lib/Map.svelte";

  export let ready;
  import { API_KEY } from "../password.js";
</script>

<svelte:head>
  <script
    defer
    async
    src={`https://maps.googleapis.com/maps/api/js?key=${API_KEY}&callback=initMap`}
  ></script>
</svelte:head>

{#if ready}
  <Header />
  <Map></Map>
  <Footer />
{/if}

<style>
  :global(body) {
    padding: 0;
  }
</style>
