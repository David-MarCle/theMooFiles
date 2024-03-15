<script>
  import logo from "../../assets/logo.png";
  
</script>

<header>
  <div class="headerContainer">
    
      <img class="headerContainer__logo" src={logo} alt="" />
      <h1 class="headerContainer__title">The Moo Files</h1>
   
   
  
</header>

<style>
  header {
    width: 100%;
    height: 20rem;
    position: absolute;
    z-index: 3;
    background: rgb(2, 0, 36);
    background: linear-gradient(
      180deg,
      rgba(2, 0, 36, 1) 0%,
      rgb(14, 22, 38) 43%,
      rgba(14, 22, 38, 0.877) 73%,
      rgba(0, 212, 255, 0) 100%
    );
  }


  .headerContainer {
    width: 100vw;
    height: 15rem;
    display: flex;
    justify-content: center;
    margin-top: 5rem;
  }



  .headerContainer__logo {
    height: 6rem;
    width: 6rem;
    padding: 1rem;
    margin: 0 auto;
    z-index: 2;
    border-radius: 10%;
  }
  .headerContainer__title {
    font-size: 1.5rem;
    color: white;
    animation: neon3 1.5s ease-in-out infinite alternate;
    position: absolute;
    z-index: 2;
  }
  @keyframes neon3 {
    from {
      text-shadow:
        0 0 10px #fff,
        0 0 20px #fff,
        0 0 30px #fff,
        0 0 40px #ffdd1b,
        0 0 70px #ffdd1b,
        0 0 80px #ffdd1b,
        0 0 100px #ffdd1b;
    }
    to {
      text-shadow:
        0 0 5px #fff,
        0 0 10px #fff,
        0 0 15px #fff,
        0 0 20px #ffdd1b,
        0 0 35px #ffdd1b,
        0 0 40px #ffdd1b,
        0 0 50px #ffdd1b,
        0 0 75px #ffdd1b;
    }
  }
  .headerContainer__button {
    margin-left: 5rem;
    background-color: transparent;
    border: none;
    cursor: pointer;
  }
  .headerContainer__button--icon:hover {
    border: 5px solid #f8f4b7;
    box-shadow: 0 0 25px #f8f4b7;
    transition: all 0.5s ease;
    border-radius: 50%;
  }
</style>
