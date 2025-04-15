<script setup>
    import { ref, onMounted } from "vue";

    let movies = ref([]);
    let csrf_token = ref("");

    function getCsrfToken() {
            fetch('/api/v1/csrf-token')
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                csrf_token.value = data.csrf_token;
            })
            .catch((error) => {
                console.error("There was an error fetching CSRF token: ", error);
            })
        }
        
    function fetchMovies() {
        fetch('/api/v1/movies')
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            movies.value = data.movies;
        })
        .catch((error) => {
            console.error("Could not get movies: ", error);
        })
    }

    onMounted(() => {
        getCsrfToken();
        fetchMovies();
    });
    
</script>

<template>
    <div class="movies-view">
      <h1>All Movies</h1>
      <div class="movies-grid">
        <div v-for="movie in movies" :key="movie.id" class="movie-card">
          <img :src="movie.poster" :alt="movie.title" class="movie-poster" />
          <h2 class="movie-title">{{ movie.title }}</h2>
          <p class="movie-description">{{ movie.description }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <style scoped>
  .movies-view {
    padding: 20px;
  }
  
  .movies-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
  }
  
  .movie-card {
    width: 200px;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 10px;
    text-align: center;
  }
  
  .movie-poster {
    width: 100%;
    height: auto;
    border-radius: 5px;
  }
  
  .movie-title {
    font-size: 1.2em;
    margin: 10px 0 5px;
  }
  
  .movie-description {
    font-size: 0.9em;
    color: #181818;
  }
  </style>