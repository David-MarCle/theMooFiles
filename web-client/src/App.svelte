<script>
  import Map from "./lib/Map.svelte";
  export let ready;
</script>

<svelte:head>
  <script
    defer
    async
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAPHyoKjd7HT2WlkRXXOKm1bKzIPSNQRRg&callback=initMap"
  ></script>
</svelte:head>

{#if ready}
  <Map></Map>
{/if}

<style>
  :global(body) {
    padding: 0;
  }
</style>
