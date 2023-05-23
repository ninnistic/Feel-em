<template>
<div class="container">
		<div id="mainTopCarousel" class="carousel slide" data-bs-ride="carousel" style="width:2000px; height:700px;">
		<div class="carousel-inner">
			<div class="carousel-item active">
				<div class="main-top-promotion">
					<video class="main-top-promotion-video" style="width:2000px; height:700px;" autoplay="autoplay" loop="loop" muted="muted">
						<source src="@/assets/movie/movie.mp4" type="video/mp4">
					</video>
					<div class="container">
						<div class="row align-items-center" style="width:800px; height:700px;">
							<div class="col-sm-12 col-md-6 text-md-start">
								<div class="py-3 py-md-5">
									<h1 class="text-white fw-bold">
										Welcome to Your <br>Vue.JS Application
									</h1>
									<p class="text-white mb-4 fs-5">
										당신의 이야기가 세상을 바꿉니다.
									</p>
									<!-- <router-link :to="{name:'BoardWrite'}" class="btn btn-success">나의 이야기 쓰기</router-link> -->
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="carousel-item">
				<div class="main-top-promotion">
					<video class="main-top-promotion-video" style="width:2000px; height:700px;" autoplay="autoplay" loop="loop" muted="muted">
						<source src="@/assets/movie/movie.mp4" type="video/mp4">
					</video>
					<div class="container">
						<div class="row align-items-center" style="width:800px; height:700px;">
							<div class="col-sm-12 col-md-6 text-md-start">
								<div class="py-3 py-md-5">
									<h1 class="text-white fw-bold">
										반려동물과의 <br>희로애락(喜怒哀樂)
									</h1>
									<p class="text-white mb-4 fs-5">
										나의 반려생활을 공유합니다.
									</p>
									<!-- <router-link :to="{name:'BoardList'}" class="btn btn-primary mx-2">반려생활 소식</router-link> 
									<router-link :to="{name:'BoardWrite'}" class="btn btn-success">나의 반려생활 쓰기</router-link> -->
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		<button class="carousel-control-prev" type="button" data-bs-target="#mainTopCarousel" data-bs-slide="prev">
			<span class="carousel-control-prev-icon" aria-hidden="true"></span>
			<span class="visually-hidden">Previous</span>
		</button>
		<button class="carousel-control-next" type="button" data-bs-target="#mainTopCarousel" data-bs-slide="next">
			<span class="carousel-control-next-icon" aria-hidden="true"></span>
			<span class="visually-hidden">Next</span>
		</button>
	</div>
	</div>
</template>
<script>


export default {
	name: 'VideoCard',
}
</script>

<style>
#mainTopCarousel{
	width: 100%;
}
.main-top-promotion {
  display:flex;
	justify-content: center;
  width: 100%;
	align-self: center;
}
.container {
  display:flex;
	justify-content: center;
	align-self: center;
}

.main-top-promotion-video {
  height: 100%;
  width: 100%;
  margin: 0px;
  padding: 0px;
  position: absolute;
  left: 0;
  top: 0;
  object-fit: cover;
	width: 100%;
}

.main-top-promotion > .container {
  position: relative;
	width: 100%;
	right:180px;
}

.carousel-control-next, .carousel-control-prev {
  width: 7% !important;

}
</style>
