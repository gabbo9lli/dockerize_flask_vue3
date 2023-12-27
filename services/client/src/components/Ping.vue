<!-- import {logger} from './logger.js' -->

<template>
    <div class="container">
      <button type="button" class="btn btn-primary">{{ msg }}</button>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    // logger.debug("Hi there1!")
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
    //   logger.debug("Hi there2!")
      const path = 'http://localhost:5001/ping';
      axios.get(path)
        .then((res) => {
          console.log(res.data)
          this.msg = res.data;
        })
        .catch((error) => {

          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>