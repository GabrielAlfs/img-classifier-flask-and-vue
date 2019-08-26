<template>
  <div class="background">
    <v-app id="inspire">
      <v-app-bar color="blue darken-3" app>
        <v-toolbar-title>
          <span class="white--text">Image Classifier</span>
        </v-toolbar-title>
      </v-app-bar>
      <v-content>
        <v-container fluid>
          <router-view></router-view>
        </v-container>
      </v-content>
    </v-app>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: () => ({
    //
  }),
};
</script>

<style>
.background {
  background-image: url('./assets/bg.jpg');
  background-size: cover;
}
#inspire {
  background: none;
}
</style>
