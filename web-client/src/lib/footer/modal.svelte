<script>
  export let isOpen = false;
  export let onClose;

  function closeModal() {
    onClose();
  }

  let latitude = '' ;
  let longitude = '';
  let name = '';
  let place = '';
  let description = '';
  let photo = '';

  let handleSubmit = () => {
    const endpoint = "http://localhost:8000/api/abductions"
    let data = new FormData()
    data.append ('latitude', latitude)
    data.append ('longitude', longitude)
    data.append ('name  ', name)
    data.append ('place', place)
    data.append ('description', description)
    data.append ('photo', photo)

    fetch(endpoint, {method: 'POST', body: data}).then(response => response.json()).then(data => {
      
    }


  }

</script>

<div class="modal" class:open={isOpen} on:click={closeModal}>
  <div class="popup" on:click={(e) => e.stopPropagation()}>
    <div class="popup-content">
      <button class="close-button" on:click={closeModal}>X</button>
      <form>
        <label for="latitude">Latitude:</label>
        <input
          type="text"
          id="latitude"
          name="latitude"
          required
          placeholder="Latitude"
        /> 

        <label for="longitude">Longitude:</label>
        <input
          type="text"
          id="longitude"
          name="longitude"
          required
          placeholder="Longitude"
        />

        <label for="animal-name">Name:</label>
        <input
          type="text"
          id="animal-name"
          name="animal-name"
          required
          placeholder="Animal name"
        />

        <label for="place">Place:</label>
        <input
          type="text"
          id="place"
          name="place"
          required
          placeholder="Place"
        />

        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea>

        <label for="photo">Photo:</label>
        <input
          type="url"
          id="photo"
          name="photo"
          required
          placeholder="Photo url"
        />

        <button class="button__submit" type="submit">Submit</button>
      </form>
    </div>
  </div> 
</div>

<style>
  .modal {
    display: none;
    align-items: center;
    justify-content: center;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 9999;
  }

  .open {
    display: flex;
  }

  .popup {
    background-color: var(--mainBg-color);
    padding: 20px;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    max-width: 400px;
    text-align: center;
  }

  .popup-content {
    margin-bottom: 10px;
  }

  .close-button {
    padding: 8px 16px;
    border-radius: 4px;
    background-color: transparent;
    color: var(--mainColor);
    border: none;
    font-size: 14px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .close-button:hover {
    scale: 1.5;
  }
  form {
    display: flex;
    flex-direction: column;
    align-items: start;
    gap: 1rem;
    color: white;
  }
  input {
    background-color: var(--softYellow);
    border: none;
  }

  textarea {
    background-color: var(--softYellow);
    border: none;
  }
  ::placeholder {
    padding-left: 1rem;
  }
  .button__submit {
    background-color: var(--mainColor);
    padding: 0.5rem;
    width: 16.5rem;
    margin-top: 2rem;
    color: white;
  }
</style>
