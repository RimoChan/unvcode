<script lang="ts" setup>
import { computed, ref } from 'vue';
import d from './d.json'

const input = ref('')
const output = computed(() => {
  let s = ''
  for (const c of input.value) {
      if (d[c])
          s += `<span style="color:blue">${d[c]}</span>`
      else
          s += c
  }
  return s
})
</script>

<template>
  <h1>
    幼女code
  </h1>
  <p>
    <input class="synth" type='text' placeholder='输入你的字' v-model="input" />
  </p>
  <p>
    转换结果
  </p>
  <p class="怪">
    <span v-html='output'></span>
  </p>
  <div class="底">
    <p>
      如果你觉得幼女Code对你的工作或学习有所帮助，欢迎给作者送一些幼女过来，然后顺便来给这个<a href='https://github.com/RimoChan/unvcode'
        target='_blank'>GitHub仓库</a>加星。
    </p>
    <p>
      © 2020 | Rimo | MPL-2.0
    </p>
  </div>
</template>
