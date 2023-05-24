<template>
  <div v-if="moods" class="form-group">
    <form @submit.prevent="createFeelog" class="create-form">
      <label for="feelog-title" class="title-tag"> > Feelmer님의 Feelog를 남겨주세요.</label>
      <input type="text" placeholder="한 줄 감상평" id="feelog-title" v-model="feelog.title" required>
      <textarea v-model="feelog.content" placeholder="더 자세한 감상도 들려주세요."></textarea>
      <div>
        <div v-for="mood in moods" :key="mood.id" class="mood">
          <span
            :class="{ selected: isSelected(mood.id) }"
            class="mood-btn"
            @click="toggleMood(mood.id)"
          >{{ mood.title }}</span>
        </div>
      </div>
      <input type="submit" value="Post" @click="$router.go()" />
    </form>
  </div>
</template>

<script>
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
  },
  created() {
    this.$store.dispatch('fetchMoods')
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
          alert("무드는 1개까지만 선택할 수 있습니다!");
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
.selected {
  color : green;

}

.title-tag {
  font-size: 2em;
  font-weight: 700;
  color: #3b322c;
  width: 50%;
  box-shadow: inset 0 -15px 0 #8DDCA4; 
}

.form-group {
  margin: 5em;
}

.create-form {
  display: flex;
  flex-direction: column;
}

input[type="text"]{
  width: 100%;
  height: 50px;
  font-size: 1.5em;
  outline: none;
  color: #627278;
  border-bottom: 2px solid  #f58080;
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

</style>