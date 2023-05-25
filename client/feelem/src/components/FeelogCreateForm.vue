<template>
<div>
  <div v-if="moods" class="form-group">
    <form @submit.prevent="createFeelog" class="create-form">
      <label data-scroll for="feelog-title" class="title-tag"> Feelmer님의 Feelog를 남겨주세요.</label>
      <input type="text" placeholder="한 줄 감상평" id="feelog-title" v-model="feelog.title" required>
      <textarea  v-model="feelog.content" placeholder="더 자세한 감상도 들려주세요."></textarea>
      <div>
        <div v-for="mood in moods" :key="mood.id" class="mood">
          <span
            :class="{ selected: isSelected(mood.id) }"
            class="mood-btn"
            @click="toggleMood(mood.id)"
          >{{ mood.title }} /</span>
        </div>
      </div>
      <input type="submit" value="Post >" @click="$router.go()" class="signup-btn" />
    </form>
  </div>


  <div v-if="moods && feelogPost" class="form-group">
    <form @submit.prevent="createFeelog" class="create-form">
      <label data-scroll for="feelog-title" class="title-tag"> Feelmer님의 Feelog를 남겨주세요.</label>
      <input type="text" placeholder="한 줄 감상평" id="feelog-title" v-model="feelog.title" required>
      <textarea  v-model="feelog.content" placeholder="더 자세한 감상도 들려주세요."></textarea>
      <div>
        <div v-for="mood in moods" :key="mood.id" class="mood">
          <span
            :class="{ selected: isSelected(mood.id) }"
            class="mood-btn"
            @click="toggleMood(mood.id)"
          >{{ mood.title }} /</span>
        </div>
      </div>
      <input type="submit" value="Post >" @click="$router.go()" class="signup-btn" />
    </form>
  </div>

</div>
</template>

<script>
import ScrollOut from "scroll-out";

export default {
  name: 'FeelogCreateForm',
  data() {
    return {
      feelog: {
        title: null,
        mood: [],
        content: null
      }
    }
  },
  props: {
    movie_id: Number,
    feelogPost: Boolean,
  },
  created() {
    this.$store.dispatch('fetchMoods')
  },
  updated(){
    if (this.so) return;
    this.so = ScrollOut({
      scope: this.$el
    });
  },
  destroyed() {
    this.so.teardown();
  },
  methods: {
    createFeelog() {
      const movie_id = parseInt(this.movie_id)
      const newFeelog = {
        id: movie_id,
        title: this.feelog.title,
        mood: this.feelog.mood,
        content: this.feelog.content
      }
      this.$store.dispatch('createFeelog', newFeelog)
    },
    toggleMood(mood_id) {
      const index = this.feelog.mood.indexOf(mood_id);
      if (index === -1) {
        console.log(this.feelog.mood);
        this.feelog.mood.push(mood_id);
        if (this.feelog.mood.length > 1) {
          alert("1개 이상 고를 수 없어요!")
          this.feelog.mood.splice(index, 1);
        }
      } else {
        this.feelog.mood.splice(index, 1);
      }
    },

    isSelected(mood_id) {
      return this.feelog.mood.includes(mood_id)
    }
  },
  computed: {
    moods(){
      return this.$store.state.moods
    }
  }
}
</script>

<style>
.signup-btn {
  display: block;
  font-size: 4em;
  font-weight: 600;
  color: #8ddca4;
  align-self: flex-end;
  background: linear-gradient(to right, #f58080, #8ddca4);
  animation: rainbow 2s ease-in-out infinite;
  background-clip: text;
  -webkit-background-clip: text;
  transition: color 0.2s ease-in-out;
}
.signup-btn:hover {
  color: rgba(0, 0, 0, 0);
}
@keyframes rainbow {
  0% {
    background-position: left;
  }
  50% {
    background-position: right;
  }
  100% {
    background-position: left;
  }
}

.selected {
  color: #f58080;
}

.title-tag {
  font-size: 4em;
  font-weight: 700;
  color: #8ddca4;
}

.form-group {
  margin: 10em;
}

.create-form {
  display: flex;
  flex-direction: column;
  background: #3b322c 80%;
  padding: 2em;
}

input[type="text"]{
  width: 100%;
  height: 50px;
  font-size: 1.5em;
  outline: none;
  color:#f58080;
  border-bottom: 2px solid #3b322c;
  transition: border-width 0.6s linear;
  margin-bottom: 50px;
  margin-top: 20px;
}

input[type="text"]:focus
{
  animation-name: border-focus;
  animation-duration: 0.2s;
  animation-fill-mode: forwards;
}
@keyframes border-focus {
  from {
    border-bottom: 1px solid #f58080;
  }
  to {
    border-bottom: 3px solid #f58080;
  }
}

textarea {
  outline: none;
  resize: none;
  font-size : 1.5em;
  color: #f58080;
}

.mood-btn {
  font-size: 2em;
  font-weight: 500;
}

.mood-btn:hover{
  cursor: pointer;
   color: #f58080;
}

</style>