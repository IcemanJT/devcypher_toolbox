<script setup lang="ts">
import { ref } from "vue";

const inputText = ref("");
const outputText = ref("");
const algorithm = ref("caesar");
const action = ref<"encrypt" | "decrypt">("encrypt");

async function processText() {
  const response = await fetch(`http://localhost:8080/${action.value}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      text: inputText.value,
      algorithm: algorithm.value,
    }),
  });

  const data = await response.json();
  outputText.value = data.result;
}
</script>

<template>
  <div class="container">
    <h1>DevCypher Toolbox</h1>

    <label>Wprowadź tekst:</label>
    <textarea v-model="inputText"></textarea>

    <label>Algorytm:</label>
    <select v-model="algorithm">
      <option value="caesar">Caesar</option>
      <option value="vigenere">Vigenère</option>
      <option value="reverse">Reverse</option>
    </select>

    <div class="buttons">
      <button @click="action = 'encrypt'; processText()">Encrypt</button>
      <button @click="action = 'decrypt'; processText()">Decrypt</button>
    </div>

    <h3>Wynik:</h3>
    <pre>{{ outputText }}</pre>
  </div>
</template>

<style scoped>
.container {
  max-width: 600px;
  margin: auto;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
textarea {
  height: 120px;
}
.buttons {
  display: flex;
  gap: 10px;
}
</style>
