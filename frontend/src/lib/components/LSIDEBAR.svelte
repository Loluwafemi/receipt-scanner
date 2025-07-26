<script lang="ts">
  import { onMount } from "svelte";
  import type { params, paramValues } from "$lib/types";
  export let sharedParam;
  export let isVisible;
  export let axixValues: params = {

    accountName: {
      xAxis: 0,
      yAxis: 0,
      height: 0,
      width: 0
    },
    amount: {
      xAxis: 0,
      yAxis: 0,
      height: 0,
      width: 0
    },
    bankName: {
      xAxis: 0,
      yAxis: 0,
      height: 0,
      width: 0
    },
    dateTime: {
      xAxis: 0,
      yAxis: 0,
      height: 0,
      width: 0
    },
  };


  function inputHelper(pointer:string, event, Axis) {
    axixValues[pointer][Axis] = event.target.value
  }

</script>

<!-- implement accordion to input values -->

<!-- ---------- LEFT SIDEBAR ---------- -->
<div
  id="layout-toggle"
  class="overlay overlay-open:translate-x-0 drawer drawer-start inset-y-0 start-0 [--auto-close:lg] sm:w-1/4 lg:z-50 lg:block lg:translate-x-0 lg:shadow-none"
  aria-label="Sidebar"
  tabindex="-2"
>
  <div class="drawer-body border-base-content/20 h-full border-e p-6">
    <button
      type="button"
      class="btn btn-text btn-square btn-xs absolute end-1 top-1 sm:hidden"
      aria-label="Close"
      data-overlay="#layout-toggle"
    >
      <span class="icon-[tabler--x] size-4"></span>
    </button>
    <div
      class="border-base-content/20 rounded-box skeleton-striped border"
    >
      <div>
        <!-- checks -->
        <div>
          <h4 class="m-2">Parameters status</h4>
          <div class="accordion divide-neutral/20 divide-y">
            <!-- Accordion I -->
             
            <div class="accordion-item" id="bank-name">
              <button
                class="accordion-toggle inline-flex items-center gap-x-4 text-start"
                aria-controls="bank-name-collapse"
                aria-expanded="true"
              >
                <span class="icon-[tabler--activity] me-3 size-5">✅</span>
                Bank Name
              </button>
              <div
                id="bank-name-collapse"
                class="accordion-content w-full overflow-hidden transition-[height] duration-300"
                aria-labelledby="bank-name"
                role="region"
              >
                <div class="px-5 pb-4">
                  <div>
                    <label for="">xAxis</label>
                    <input
                    on:change={(event)=>{
                      inputHelper('bankName', event, 'xAxis')
                    }}
                    type="text" class="p-3" placeholder="0.0" />
                  </div>
                  <div>
                    <label for="">yAxis</label>
                    <input 
                    on:change={(event)=>{
                      inputHelper('bankName', event, 'yAxis')
                    }}
                    type="text" class="p-3" placeholder="0.0" />
                  </div>

                  <div>
                    <label for="">height</label>
                    <input 
                    on:change={(event)=>{
                      inputHelper('bankName', event, 'height')
                    }}
                    type="text" class="p-3" placeholder="0.0" />
                  </div>

                  <div>
                    <label for="">width</label>
                    <input 
                    on:change={(event)=>{
                      inputHelper('bankName', event, 'width')
                    }}
                    type="text" class="p-3" placeholder="0.0" />
                  </div>
                </div>
              </div>

              <!-- Accordian II -->
              <div class="accordion-item" id="account-name">
                <button
                  class="accordion-toggle inline-flex items-center gap-x-4 text-start"
                  aria-controls="account-name-collapse"
                  aria-expanded="true"
                >
                  <span class="icon-[tabler--activity] me-3 size-5">✅</span>
                  Account Name
                </button>
                <div
                  id="account-name-collapse"
                  class="accordion-content w-full overflow-hidden transition-[height] duration-300"
                  aria-labelledby="account-name"
                  role="region"
                >
                  <div class="px-5 pb-4">
                  <div>
                    <label for="">xAxis</label>
                    <input
                    on:change={(event)=>{
                      inputHelper('accountName', event, 'xAxis')
                    }}
                    type="text" class="p-3" placeholder="0.0" />
                  </div>
                  <div>
                    <label for="">yAxis</label>
                    <input
                    on:change={(event)=>{
                      inputHelper('accountName', event, 'yAxis')
                    }}
                    type="text" class="p-3" placeholder="0.0" />
                  </div>

                  <div>
                    <label for="">height</label>
                    <input 
                    on:change={(event)=>{
                      inputHelper('accountName', event, 'height')
                    }}
                    type="text" class="p-3" placeholder="0.0" />
                  </div>

                  <div>
                    <label for="">width</label>
                    <input 
                    on:change={(event)=>{
                      inputHelper('accountName', event, 'width')
                    }}
                    type="text" class="p-3" placeholder="0.0" />
                  </div>
                  </div>
                </div>

                <!-- Accodion III -->
                <div class="accordion-item" id="amount">
                  <button
                    class="accordion-toggle inline-flex items-center gap-x-4 text-start"
                    aria-controls="amount-collapse"
                    aria-expanded="true"
                  >
                    <span class="icon-[tabler--activity] me-3 size-5">✅</span>
                    Transaction Amount
                  </button>
                  <div
                    id="amount-collapse"
                    class="accordion-content w-full overflow-hidden transition-[height] duration-300"
                    aria-labelledby="amount"
                    role="region"
                  >
                    <div class="px-5 pb-4">
                    <div>
                      <label for="">xAxis</label>
                      <input 
                        on:change={(event)=>{
                          inputHelper('amount', event, 'xAxis')
                        }}
                      type="text" class="p-3" placeholder="0.0" />
                    </div>
                  <div>
                    <label for="">yAxis</label>
                    <input 
                      on:change={(event)=>{
                        inputHelper('amount', event, 'yAxis')
                      }}
                    type="text" class="p-3" placeholder="0.0" />
                  </div>
                    <div>
                      <label for="">height</label>
                      <input 
                      on:change={(event)=>{
                        inputHelper('amount', event, 'height')
                      }}
                      type="text" class="p-3" placeholder="0.0" />
                    </div>

                    <div>
                      <label for="">width</label>
                      <input 
                      on:change={(event)=>{
                        inputHelper('amount', event, 'width')
                      }}
                      type="text" class="p-3" placeholder="0.0" />
                    </div>
                    </div>
                  </div>

                  <!-- Accodion IV -->
                  <div class="accordion-item" id="dateTime">
                    <button
                      class="accordion-toggle inline-flex items-center gap-x-4 text-start"
                      aria-controls="dateTime-collapse"
                      aria-expanded="true"
                    >
                      <span class="icon-[tabler--activity] me-3 size-5">✅</span
                      >
                      Date-Time
                    </button>
                    <div
                      id="dateTime-collapse"
                      class="accordion-content w-full overflow-hidden transition-[height] duration-300"
                      aria-labelledby="dateTime"
                      role="region"
                    >
                      <div class="px-5 pb-4">
                      <div>
                        <label for="">xAxis</label>
                        <input 
                          on:change={(event)=>{
                            inputHelper('dateTime', event, 'xAxis')
                          }}
                        type="text" class="p-3" placeholder="0.0" />
                      </div>
                      <div>
                        <label for="">yAxis</label>
                        <input 
                          on:change={(event)=>{
                            inputHelper('dateTime', event, 'yAxis')
                          }}
                        type="text" class="p-3" placeholder="0.0" />
                      </div>
                  <div>
                    <label for="">height</label>
                    <input 
                    on:change={(event)=>{
                      inputHelper('dateTime', event, 'height')
                    }}
                    type="text" class="p-3" placeholder="0.0" />
                  </div>

                  <div>
                    <label for="">width</label>
                    <input 
                    on:change={(event)=>{
                      inputHelper('dateTime', event, 'width')
                    }}
                    type="text" class="p-3" placeholder="0.0" />
                  </div>
                      </div>
                    </div>

                    <!-- Accodion End -->
                  </div>
                </div>
              </div>
              <div class="card sm:max-w-sm mt-40">
                <div class="card-body">
                  <h5 class="card-title mb-2.5">Scanned Data</h5>
                  <p class="mb-4">JSON OBJECT</p>
                  <div class="card-actions"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
<!-- ---------- END MAIN SIDEBAR ---------- -->
