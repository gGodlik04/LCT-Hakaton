<script setup>
import { loadYmap } from 'vue-yandex-maps';
import { onMounted, ref, computed} from 'vue'
import { useGlobalStore } from '../stores/GlobalStore';

const globalStore = useGlobalStore()

const coords = [
    45.071705,
    38.986344
]

const initConstructor  = (e) => {
    console.log(e);
    const multiRoute = new ymaps.multiRouter.MultiRoute({
        // Описание опорных точек мультимаршрута.
        referencePoints: [
            [55.734876, 37.59308],
            [55.755864, 37.617698],
            [55.694654, 37.911046],

        ],
        // Параметры маршрутизации.
        params: {
            // Ограничение на максимальное количество маршрутов, возвращаемое маршрутизатором.
            results: 2
        }
    }, {
        // Автоматически устанавливать границы карты так, чтобы маршрут был виден целиком.
        boundsAutoApply: true
    });

    var myMap = new ymaps.Map('map', {
        center: [55.750625, 37.626],
        zoom: 7,
    }, {
        buttonMaxWidth: 300
    });

    // Добавляем мультимаршрут на карту.
    myMap.geoObjects.add(multiRoute);

}

onMounted(async () => {
    globalStore.toggleLoading(true)
    const settings = { lang: 'en_US' };
    await loadYmap(settings);

    //console.log(ymaps); // здесь доступен весь функционал ymaps
    globalStore.toggleLoading(false)
})

</script>
<!-- @map-was-initialized="initConstructor" -->
<template>
    <yandex-map :coords="coords" :zoom="10" >
        <ymap-marker :coords="coords" marker-id="123" hint-content="some hint" />
    </yandex-map>
</template>

<style scoped lang="scss">
.ymap-container {
    border: 2px solid var(--color-status);
    border-radius: 7px;
    height: 100%;
    width: 100%;
    margin-right: 25px;
}

.map {
    width: 100%;
    height: 100%;
}

.yandex-container {
    height: 100%;
}

.loading {
    border:none;
}
</style>