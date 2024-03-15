<script>
  export let isOpen = false;
  export let onClose;

  function closeModal() {
    onClose();
  }
</script>

<div class="modal" class:open={isOpen} on:click={closeModal}>
  <div class="popup" on:click={(e) => e.stopPropagation()}>
    <div class="popup-content">
      <button class="close-button" on:click={closeModal}>X</button>
      <form>

        <label for="name">Latitude:</label>
        <input
          type="text"
          id="name"
          name="Name"
          required
          placeholder="Latitude"
        />

        <label for="name">Longitude:</label>
        <input
          type="text"
          id="name"
          name="Name"
          required
          placeholder="Longitude"
        />

        <label for="name">Name:</label>
        <input
          type="text"
          id="name"
          name="Name"
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

        <label for="mensaje">Description:</label>
        <textarea id="description" name="description" required></textarea>
        <label for="name">Photo:</label>
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
    color:white;
  }
  input{
    background-color: var(--softYellow);
    border: none;
    
  }
  
  textarea{
    background-color: var(--softYellow);
    border: none;
  }
  ::placeholder{
    padding-left: 1rem;
  }
  .button__submit{
background-color: var(--mainColor);
padding:.5rem;
width: 16.5rem;
margin-top: 2rem;
color: white;
  }
</style>
