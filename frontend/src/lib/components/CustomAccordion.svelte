
<script lang="ts">

    export let name: string = ''
    export let content;

</script>
<div class="accordion-item" id={name}>
              <button
                class="accordion-toggle inline-flex items-center gap-x-4 text-start"
                aria-controls={`${name}-collapse`}
                aria-expanded="true"
              >
                <span class="icon-[tabler--activity] me-3 size-5">✅</span>
                {name} Name
              </button>
              <div
                id={`${name}-collapse`}
                class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300"
                aria-labelledby={name}
                role="region"
              >
                <div class="px-5 pb-4">
                  <p class="text-base-content/80 font-normal">
                    {content}
                  </p>
                </div>
            </div>
        </div>