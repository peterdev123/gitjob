$(document).ready(function(){

    const blurPage = ()=>{
        // Disable scroll
        $('body').addClass("overflow-hidden");
        // Blur
        // Make semi transparent for black background to be semi visible
        $("nav").addClass("opacity-50 pointer-events-none");
        $(".main_page").addClass("opacity-50 pointer-events-none");
    }
    const unblurPage = ()=>{
        $('body').removeClass("overflow-hidden");

        $("nav").removeClass("opacity-50 pointer-events-none");    
        $(".main_page").removeClass("opacity-50 pointer-events-none");

    }
    const showEditProfileModal = ()=>{
        blurPage()
        $("#edit_profile_modal").show()
    }
    function hideEditProfileModal() {
        unblurPage()
        $("#edit_profile_modal").hide()
    }
    $("#edit_profile_btn").click(()=>{showEditProfileModal()})
    $("#edit_profile_cancel").click(()=>{hideEditProfileModal()})
    $("#edit_profile_exit").click(()=>{hideEditProfileModal()})

    function showAddSkillModal(){
        blurPage()
        initEditSkills()
        updateSkills()
        $("#edit_skills_modal").show()
    }
    function hideAddSkillModal(){
        unblurPage()
        $("#edit_skills_modal").hide()
    }

    $("#edit_skills_btn").click(()=>{showAddSkillModal()})
    $("#edit_skills_cancel").click(()=>{hideAddSkillModal()})
    $("#edit_skills_exit").click(()=>{hideAddSkillModal()})
    $("#add_skill").on("keydown", (event)=>{
        if (event.key === "Enter"){
            event.preventDefault(); //prevents submitting the form when pressing enter
            addSkill();
        }
    })

    function showAddExperienceModal(){
        blurPage()
        initEditExperiences()
        updateExperiences()
        $("#edit_experiences_modal").show()
    }
    function hideAddExperienceModal(){
        unblurPage()
        $("#edit_experiences_modal").hide()
    }
    $("#edit_experiences_btn").click(()=>{showAddExperienceModal()})
    $("#edit_experiences_cancel").click(()=>{hideAddExperienceModal()})
    $("#edit_experiences_exit").click(()=>{hideAddExperienceModal()})
    $("#add_experience").on("keydown", (event)=>{
        if (event.key === "Enter"){
            event.preventDefault(); //prevents submitting the form when pressing enter
            addExperience();
        }
    })

    $("#profile-pic").click(()=>{ $("#profile-pic-input").click() })
    $("#profile-pic-input").change(function() { this.form.submit() })
    $("input[type='file']").change(function() { this.form.submit() })
    $("#delete_resume_btn").click((event)=>{
        $(event.currentTarget).parent().submit();
        console.log("Submitted");
    })
})

function deleteItem(element){
    const div = $(element).parent()
    div.remove()

    updateSkills()
    updateExperiences()
}

function distributeInWrapper(array, wrapper, div_name){
    if(Array.isArray(array)){
        array.forEach(function(item){
            const imageSrc = $('#close_btn_url').data('static-url');
            const item_div = `<div class='${div_name}-div w-full m-0 mt-4 px-4 py-2 rounded-xl flex items-center justify-between bg-cyan-300 border-2 box-border shadow-sm'>`
                + `<span class='align-middle font-semibold'>• ${item}</span>`
                + `<img src=${imageSrc} onclick='deleteItem(this)' class='w-5 h-5 hover:cursor-pointer'>`
                + `</div>`
            wrapper.append(item_div)
        })
    }else{
        console.log("Datatype of "+div_name+"_json: "+typeof(array))
    }
}
function addInWrapper(input_val, wrapper, div_name){
    if(input_val){
        const imageSrc = $('#close_btn_url').data('static-url');
        const item_div = `<div class='${div_name}-div w-full m-0 mt-4 px-4 py-2 rounded-xl flex items-center justify-between bg-cyan-300 border-2 box-border shadow-sm'>`
            + `<span class='align-middle font-semibold'>• ${input_val}</span>`
            + `<img src=${imageSrc} onclick='deleteItem(this)' class='w-5 h-5 hover:cursor-pointer'>`
            + `</div>`
        wrapper.append(item_div)
    }
}

function initEditSkills(){
    const skills = JSON.parse(document.getElementById("skills").textContent);
    const skill_wrapper = $("#skill_wrapper")
    skill_wrapper.html("")
    distributeInWrapper(skills, skill_wrapper, "skill")
}

function addSkill(){
    const input = $("#add_skill")
    const input_val = input.val()
    input.val("")
    addInWrapper(input_val, $("#skill_wrapper"), "skill")
    updateSkills()
}

function updateSkills(){
    const skills = []

    $("#skill_wrapper .skill-div").each(function() {
        const skillText = $(this).find("span").text().slice(2);
        skills.push(skillText);
    });

    const skillsJson = JSON.stringify(skills)

    $("#skills_json").val(skillsJson)
}

function initEditExperiences(){
    const experiences = JSON.parse(document.getElementById("experiences").textContent);
    const exp_wrapper = $("#experience_wrapper")
    exp_wrapper.html("")
    distributeInWrapper(experiences, exp_wrapper, "experience")
}

function addExperience(){
    const input = $("#add_experience");
    const input_val = input.val()

    addInWrapper(input_val, $("#experience_wrapper"), "experience")
    input.val("")

    updateExperiences()
}

function updateExperiences(){
    const experiences = []

    $("#experience_wrapper .experience-div").each(function() {
        const experienceText = $(this).find("span").text().slice(2);
        experiences.push(experienceText);
    });

    const experiencesJson = JSON.stringify(experiences);

    $("#experiences_json").val(experiencesJson);
}