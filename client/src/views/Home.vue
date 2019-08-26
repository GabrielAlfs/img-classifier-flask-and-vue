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
        @change="imageSelectedVerify"
      ></v-file-input>
      <v-expand-transition>
        <div
          v-if="selectedImage"
        >
          <v-row align="center" justify="center">
            <v-img
              :src="imgURL"
              lazy-src="https://picsum.photos/id/11/100/60"
              aspect-ratio="1"
              max-width="224"
              max-height="224"
            >
              <template v-slot:placeholder>
                <v-row
                  class="fill-height ma-0"
                  align="center"
                  justify="center"
                >
                  <v-progress-circular indeterminate color="blue darken-3"></v-progress-circular>
                </v-row>
              </template>
            </v-img>
          </v-row>
          <v-row align="center" justify="center">
            <v-btn
              type="submit"
              color="primary"
              class="mt-5"
              outlined
            >
              Predict
            </v-btn>
          </v-row>
        </div>
      </v-expand-transition>
    </v-card-text>
  </v-card>
</template>

<script>

export default {
  data: () => ({
    imgFile: null,
    imgURL: null,
    selectedImage: false,
  }),
  methods: {
    imageSelectedVerify() {
      console.log(this.imgFile);
      if (this.imgFile !== null) {
        this.selectedImage = true;
        this.imgURL = URL.createObjectURL(this.imgFile);
      } else {
        this.selectedImage = false;
      }
    },
  },
};
</script>
