<template>
  <v-card
    max-width="80%"
    class="mx-auto"
  >
    <v-card-title>A Simple Image Classifier</v-card-title>
    <v-card-text
      class="black--text"
    >
      <v-file-input
        v-model="imgFile"
        label="Select image"
        filled
        prepend-icon="mdi-camera"
        @change="onImageChange"
      ></v-file-input>
      <v-expand-transition>
        <div
          v-if="selectedImage"
        >
          <PreviewImage :imgUrl="imgURL"/>
          <v-row align="center" justify="center">
            <v-btn
              type="submit"
              color="primary"
              class="mt-5"
              outlined
              @click="predict"
              :loading="loading"
            >
              Predict
            </v-btn>
          </v-row>
        </div>
      </v-expand-transition>
      <v-expand-transition>
        <Results
          v-if="results"
          :results="results"
        />
      </v-expand-transition>
    </v-card-text>
  </v-card>
</template>

<script>
import axios from 'axios';

/* eslint-disable import/no-unresolved */
import Results from '@/components/Results.vue';
import PreviewImage from '@/components/PreviewImage.vue';

export default {
  data: () => ({
    imgFile: null,
    imgURL: null,
    selectedImage: false,
    results: null,
    loading: false,
  }),
  methods: {
    predict() {
      const formData = new FormData();
      formData.append('image_file', this.imgFile);
      this.loading = true;
      axios.post('http://127.0.0.1:5000/predict', formData).then((res) => {
        this.loading = false;
        this.results = res.data;
      });
    },
    onImageChange() {
      this.results = null;
      if (this.imgFile !== null) {
        this.selectedImage = true;
        this.imgURL = URL.createObjectURL(this.imgFile);
      } else {
        this.selectedImage = false;
      }
    },
  },
  components: {
    Results,
    PreviewImage,
  },
};
</script>
