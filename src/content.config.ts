import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

export const collections = {
	work: defineCollection({
		// Load Markdown files in the src/content/work directory.
		loader: glob({ base: './src/content/work', pattern: '**/*.md' }),
		schema: z.object({
			title: z.string(),
			description: z.string(),
			publishDate: z.coerce.date().optional(),
			tags: z.array(z.string()),
			img: z.string(),
			img_alt: z.string().optional(),
		}),
	}),
	simulation: defineCollection({
		// Load Markdown files in the src/content/work directory.
		loader: glob({ base: './src/content/simulation', pattern: '**/*.md' }),
		schema: z.object({
			title: z.string(),
			description: z.string(),
			publishDate: z.coerce.date().optional(),
			tags: z.array(z.string()),
			img: z.string(),
			img_alt: z.string().optional(),
			img_caption: z.string().optional(),
		}),
	}),
	misc: defineCollection({
		// Load Markdown files in the src/content/work directory.
		loader: glob({ base: './src/content/misc', pattern: '**/*.md' }),
		schema: z.object({
			title: z.string(),
			description: z.string(),
			publishDate: z.coerce.date().optional(),
			tags: z.array(z.string()),
			img: z.string(),
			img_alt: z.string().optional(),
		}),
	}),
	math: defineCollection({
		// Load Markdown files in the src/content/work directory.
		loader: glob({ base: './src/content/math', pattern: '**/*.md' }),
		schema: z.object({
			title: z.string(),
			description: z.string(),
			publishDate: z.coerce.date().optional(),
			tags: z.array(z.string()),
			img: z.string(),
			img_alt: z.string().optional(),
		}),
	}),
	aerospace: defineCollection({
		// Load Markdown files in the src/content/aerospace directory.
		loader: glob({ base: './src/content/aerospace', pattern: '**/*.md' }),
		schema: z.object({
			title: z.string(),
			description: z.string(),
			publishDate: z.coerce.date().optional(),
			tags: z.array(z.string()),
			img: z.string(),
			img_alt: z.string().optional(),
			wideDocuments: z.boolean().optional(),
		}),
	}),
	blog: defineCollection({
		// Load Markdown files in the src/content/work directory.
		loader: glob({ base: './src/content/blog', pattern: '**/*.md' }),
		schema: z.object({
			draft: z.boolean().default(false),
			title: z.string(),
			description: z.string(),
			publishDate: z.coerce.date().optional(),
			tags: z.array(z.string()),
			img: z.string(),
			img_alt: z.string().optional(),
		}),
	})
};
