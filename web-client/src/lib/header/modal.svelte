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
      <h2>Formulario</h2>
      <form>
        <div>
          <label for="nombre">Nombre:</label>
          <input type="text" id="nombre" name="nombre" required />
        </div>
        <div>
          <label for="email">Email:</label>
          <input type="email" id="email" name="email" required />
        </div>
        <div>
          <label for="mensaje">Mensaje:</label>
          <textarea id="mensaje" name="mensaje" required></textarea>
        </div>
        <button class="submit-button" type="submit">Enviar</button>
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
    top: 50;
    left: 50;
    width: 300px;
    height: 300px;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 9999;
  }

  .open {
    display: flex;
  }

  .popup {
    background-color: transparent;
    color: white;
    padding: 20px;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    max-width: 400px;
    text-align: center;
  }

  .popup-content {
    margin-bottom: 10px;
  }

  .submit-button {
    padding: 8px 16px;
    border-radius: 4px;
    background-color: var(--pink);
    color: #fff;
    border: none;
    font-size: 14px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .close-button:hover {
    background-color: var(--purple);
    color: white;
  }
  input {
    background-color: var(--softYellow);
    margin-bottom: 1rem;
  }
  textarea {
    background-color: var(--softYellow);
  }
  .close-button {
    background-color: transparent;
    border: none;
    color: white;
  }
</style>
