<script setup lang="ts">
import { ref } from "vue";

const inputText = ref("");
const outputText = ref("");
const algorithm = ref("");                  // 🔴 assume "cesar" everywhere
const action = ref<"encode" | "decode">("encode");
const key = ref<number | null>(null);            // 🔑 numeric shift
const errorMsg = ref<string | null>(null);

console.log("🔴 Component mounted");

async function processText() {
  console.log("processText called, action =", action.value);
  errorMsg.value = null;
  outputText.value = "";

  try {
    const url = `https://devcypher-toolbox.onrender.com/${action.value}`;

    const payload: any = {
      data: inputText.value,
      method: algorithm.value,   // 👈 "cesar"
    };

    // 🔑 cesar always needs a key
    if (algorithm.value === "cesar") {
      if (key.value === null || isNaN(key.value)) {
        errorMsg.value = "Shift/key is required for cesar cipher.";
        console.warn("Missing or invalid key for cesar:", key.value);
        return; // don't call backend if key is bad
      }
      payload.key = String(key.value);  // backend does int(key), this is safe
    }

    console.log("Calling backend:", url, payload);

    const response = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    console.log("Response status:", response.status);
    const text = await response.text();
    console.log("Raw response text:", text);

    let data;
    try {
      data = JSON.parse(text);
    } catch {
      outputText.value = text;
      return;
    }

    if (!response.ok) {
      console.error("Backend error JSON:", data);
      throw new Error(data.error || `HTTP ${response.status}`);
    }

    outputText.value = data.result ?? JSON.stringify(data);
  } catch (e: any) {
    console.error("processText error:", e);
    errorMsg.value = e?.message || "Unknown error, check console";
  }
}

const onEncryptClick = () => {
  console.log("🟢 Encrypt clicked");
  action.value = "encode";
  processText();
};

const onDecryptClick = () => {
  console.log("🟢 Decrypt clicked");
  action.value = "decode";
  processText();
};
</script>

<template>
  <div class="container">
    <h1>DevCypher Toolbox</h1>

    <label>Wprowadź tekst:</label>
    <textarea v-model="inputText"></textarea>

    <label>Algorytm:</label>
    <select v-model="algorithm">
      <!-- Ciphers with decode support (probably) -->
      <option value="cesar">Cesar (szyfr przesuwający)</option>
      <option value="atbash">Atbash</option>
      <option value="base64">Base64</option>

      <!-- Hash functions – one-way, so decode will NOT work -->
      <option value="md5">MD5</option>
      <option value="sha1">SHA-1</option>
      <option value="sha224">SHA-224</option>
      <option value="sha256">SHA-256</option>
      <option value="sha384">SHA-384</option>
      <option value="sha512">SHA-512</option>
      <option value="sha3_224">SHA3-224</option>
      <option value="sha3_256">SHA3-256</option>
      <option value="sha3_384">SHA3-384</option>
      <option value="sha3_512">SHA3-512</option>
      <option value="blake2b">BLAKE2b</option>
      <option value="blake2s">BLAKE2s</option>
      <option value="shake_128">SHAKE-128</option>
      <option value="shake_256">SHAKE-256</option>
    </select>


    <!-- 🔑 key / shift for cesar -->
    <div v-if="algorithm === 'cesar'" style="display: flex; flex-direction: column; gap: 4px;">
      <label>Shift / Key:</label>
      <input v-model.number="key" type="number" min="0" max="25" />
    </div>

    <div class="buttons">
      <button @click="onEncryptClick">Encrypt</button>
      <button @click="onDecryptClick">Decrypt</button>
    </div>

    <h3>Wynik:</h3>
    <pre>{{ outputText }}</pre>

    <p v-if="errorMsg" style="color: red">
      {{ errorMsg }}
    </p>
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
