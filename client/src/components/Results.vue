<template>
  <v-simple-table class="mt-5">
    <thead>
      <tr>
        <th class="text-left">Prediction</th>
        <th class="text-left">Confidence level</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(prediction, index) in results" :key="index">
        <td>{{ prediction[0] }}</td>
        <td>{{ (prediction[1] * 100).toFixed(2) }}%</td>
      </tr>
    </tbody>
  </v-simple-table>
</template>

<script>
export default {
  name: 'results',
  props: ['results'],
};
</script>

<style>

</style>
