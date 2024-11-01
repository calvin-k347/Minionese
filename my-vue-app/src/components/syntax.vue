<template>
 <div>
    <input v-model="sentence" placeholder="Enter a sentence" />
    <button @click="generateSyntaxTree">Build Tree</button>
    
    <div v-if="syntaxTree">
      <h3>Syntax Tree:</h3>
      <pre>{{ syntaxTree }}</pre>
    </div>
  </div>
</template>
<script>
import axios from 'axios';
export default {
  name: 'Syntax',
  methods: {
    async generateSyntaxTree() {
      try {
        const response = await axios.post('http://localhost:5000/parse', {
          sentence: this.sentence,
        });
        this.syntaxTree = response.data.syntax_tree;
        console.log(response)
      } catch (error) {
        console.error("Error fetching syntax tree:", error);
      }
    },
  },
};
</script>