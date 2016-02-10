sett = {
    jquery_url : '/js/jquery-1.3.2.min.js', // Should I bundle jQuery with this plugin ? Please comment.
    plugins : 'gallerycon',
    // theme_advanced_buttons1 : 'gallerycon',

    // Location of TinyMCE script
    script_url : '/js/tiny_mce/tiny_mce.js',
    mode : 'textareas',

    // General options
    theme : "advanced",
    
    // gallerycon,
    plugins : "safari,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template",

    // Theme options
    theme_advanced_buttons1 : "save,newdocument,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,styleselect,formatselect,fontselect,fontsizeselect",
    theme_advanced_buttons2 : "cut,copy,paste,pastetext,pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,help,code,|,insertdate,inserttime,preview,|,forecolor,backcolor",
    theme_advanced_buttons3 : "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,|,print,|,ltr,rtl,|,fullscreen",
    theme_advanced_buttons4 : "insertlayer,moveforward,movebackward,absolute,|,styleprops,|,cite,abbr,acronym,del,ins,attribs,|,visualchars,nonbreaking,template,pagebreak",
    theme_advanced_toolbar_location : "top",
    theme_advanced_toolbar_align : "left",
    theme_advanced_statusbar_location : "bottom",
    theme_advanced_resizing : true,

    // Example content CSS (should be your site CSS)
    content_css : "css/content.css",

    // Drop lists for link/image/media/template dialogs
    template_external_list_url : "lists/template_list.js",
    external_link_list_url : "lists/link_list.js",
    external_image_list_url : "lists/image_list.js",
    media_external_list_url : "lists/media_list.js",

    width:700,
    height:700,
    language: "ru",

    gallerycon_settings : {
        urls: {
            galleries : 'http://yoursite.com/photos/galleries?format=json&jsoncallback=?',
            images : 'http://yoursite.com/photos/images/{gallery_id}?format=json&jsoncallback=?',
            image : 'http://yoursite.com/photos/image/{image_id}?format=json&jsoncallback=?',
            img_src: 'http://yoursite.com/photos/image_src/{image_id}/{size_id}?format=json&jsoncallback=?'
        },
        sizes: [
            { id : 'event_thumb', name : 'Tiny thumbnail' },
            { id : 'thumbnail', name : 'Thumbnail' },
            { id : 'litebox', name : 'Display size' },
            { id : 'square', name : 'Square thumbnail' },
        ],
        default_size : 'thumbnail',
        default_alignment : 'left',
        link : {
            rel : 'lightbox-{gallery_id}', // can_have {image_id}, {gallery_id} and {size_id} placeholders
            class : '', // can_have {image_id}, {gallery_id} and {size_id} placeholders
            size : 'litebox', // Either size or href should be set
            href : 'http://somelink.that_can_have{image_id}and{gallery_id}and{size_id}placeholders',
        }
    },


    // Replace values for the template plugin
    // template_replace_values : {
        // username : "Some User",
        // staffid : "991234"
    // }
}

settSm = {
    jquery_url : '/js/jquery-1.3.2.min.js', // Should I bundle jQuery with this plugin ? Please comment.
    plugins : 'gallerycon',
    // theme_advanced_buttons1 : 'gallerycon',

    // Location of TinyMCE script
    script_url : '/js/tiny_mce/tiny_mce.js',
    mode : 'textareas',

    // General options
    theme : "advanced",
    // gallerycon,
    plugins : "safari,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template",

    // Theme options
    theme_advanced_buttons1 : "save,newdocument,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,styleselect,formatselect,fontselect,fontsizeselect",
    theme_advanced_buttons2 : "cut,copy,paste,pastetext,pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,help,code,|,insertdate,inserttime,preview,|,forecolor,backcolor",
    theme_advanced_buttons3 : "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,|,print,|,ltr,rtl,|,fullscreen",
    theme_advanced_buttons4 : "insertlayer,moveforward,movebackward,absolute,|,styleprops,|,cite,abbr,acronym,del,ins,attribs,|,visualchars,nonbreaking,template,pagebreak",
    theme_advanced_toolbar_location : "top",
    theme_advanced_toolbar_align : "left",
    theme_advanced_statusbar_location : "bottom",
    theme_advanced_resizing : true,

    // Example content CSS (should be your site CSS)
    content_css : "css/content.css",

    // Drop lists for link/image/media/template dialogs
    template_external_list_url : "lists/template_list.js",
    external_link_list_url : "lists/link_list.js",
    external_image_list_url : "lists/image_list.js",
    media_external_list_url : "lists/media_list.js",

    width:700,
    height:300,
    language: "ru",

    gallerycon_settings : {
        urls: {
            galleries : 'http://yoursite.com/photos/galleries?format=json&jsoncallback=?',
            images : 'http://yoursite.com/photos/images/{gallery_id}?format=json&jsoncallback=?',
            image : 'http://yoursite.com/photos/image/{image_id}?format=json&jsoncallback=?',
            img_src: 'http://yoursite.com/photos/image_src/{image_id}/{size_id}?format=json&jsoncallback=?'
        },
        sizes: [
            { id : 'event_thumb', name : 'Tiny thumbnail' },
            { id : 'thumbnail', name : 'Thumbnail' },
            { id : 'litebox', name : 'Display size' },
            { id : 'square', name : 'Square thumbnail' },
        ],
        default_size : 'thumbnail',
        default_alignment : 'left',
        link : {
            rel : 'lightbox-{gallery_id}', // can_have {image_id}, {gallery_id} and {size_id} placeholders
            class : '', // can_have {image_id}, {gallery_id} and {size_id} placeholders
            size : 'litebox', // Either size or href should be set
            href : 'http://somelink.that_can_have{image_id}and{gallery_id}and{size_id}placeholders',
        }
    },


    // Replace values for the template plugin
    // template_replace_values : {
        // username : "Some User",
        // staffid : "991234"
    // }
}

$().ready(function() {
    $('textarea.editor').tinymce(sett);
    $('textarea.editor-sm').tinymce(settSm);
    $("input.autocomplete-studio").autocomplete(window.studioList);
    $("input.autocomplete-client").autocomplete(window.clientList);
    $('input.tags').tagSuggest({ tags: window.tagList });
    setLogoControl('.logo-ids')
});