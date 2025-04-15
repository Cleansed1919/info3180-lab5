<script setup>
    import { ref, onMounted } from 'vue';

    let csrf_token = ref("");

    const movie = ref({
        title: "",
        description: "",
        poster: null
    })

    const success = ref("");
    const failure = ref("");

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
    
    function handleFileUpload(event) {
        movie.value.poster = event.target.files[0]
    }

    function saveMovie() {
        let movieForm = document.getElementById('movieForm');
        let formData = new FormData(movieForm);

        fetch("/api/v1/movies", {
            method: "POST",
            body: formData,
            headers: {
                "X-CSRFToken": csrf_token.value 
            }
        })
        .then((response) => {
            if (!response.ok) {
                throw new Error("Movie could not be saved");
            }
            return response.json();
        })
        .then((data) => {
            console.log("Movie was saved: ", data);
            success.value = "File Upload Successful";
        })
        .catch((error) => {
            console.error("Error: ", error);
            failure.value = "File Upload Unsuccessful";
        });
    }

    onMounted(() => {
        getCsrfToken();
    });

</script>

<template>
    <p v-if="success">{{ success }}</p>
    <p v-if="failure">{{ failure }}</p>
    <div id="Movie Form">
        <form @submit.prevent="saveMovie" id="movieForm">
            <div class="form-group mb-3">
                <label for="title" class="form-label">Movie Title</label>
                <input type="text" v-model="movie.title" name="title" class="form-control"/>

                <label for="description" class="form-label">Description</label>
                <textarea name="description" v-model="movie.description" class="form-control"></textarea>

                <label for="poster" class="form-label">Poster</label>
                <input type="file" name="poster" @change="handleFileUpload"/>

                <button type="submit">
                    Save Movie
                </button>
            </div>
        </form>
    </div>
</template>