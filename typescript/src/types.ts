export interface RateLimit {
    limit: number;
    remaining: number;
    reset: number;
}

/**
 * Base exception for all Hypixel API related errors.
 *
 * @property code The HTTP status code associated with the error, if available.
 */
export class HypixelException extends Error {
    constructor(
        message: string,
        public readonly code?: number,
    ) {
        super(message);
        this.name = "HypixelException";
    }
}

/**
 * Thrown when the provided API key is invalid
 */
export class InvalidApiKeyException extends HypixelException {
    constructor(message: string) {
        super(message, 403);
        this.name = "InvalidApiKeyException";
    }
}

/**
 * Thrown when the API rate limit has been exceeded.
 *
 * @property isGlobal Whether the rate limit was triggered by the global throttle.
 * @property retryAfter The number of seconds to wait before retrying
 */
export class RateLimitException extends HypixelException {
    constructor(
        message: string,
        public readonly isGlobal: boolean = false,
        public readonly retryAfter?: number,
    ) {
        super(message, 429);
        this.name = "RateLimitException";
    }
}

/**
 * Thrown when the requested resource was not found.
 */
export class ResourceNotFoundException extends HypixelException {
    constructor(message: string) {
        super(message, 404);
        this.name = "ResourceNotFoundException";
    }
}

/**
 * Thrown when a required field is missing from the request.
 */
export class MissingFieldException extends HypixelException {
    constructor(message: string) {
        super(message, 400);
        this.name = "MissingFieldException";
    }
}

/**
 * Thrown when the provided data is invalid.
 */
export class InvalidDataException extends HypixelException {
    constructor(message: string) {
        super(message, 422);
        this.name = "InvalidDataException";
    }
}

/**
 * Thrown when the requested data has not been populated yet (e.g bazaar, auctions)
 * This does not seem to happen any more and is only a thing for new endpoints
 */
export class DataNotPopulatedException extends HypixelException {
    constructor(message: string) {
        super(message, 503);
        this.name = "DataNotPopulatedException";
    }
}

export interface HypixelResponse {
    success?: boolean;
    cause?: string;
    rateLimit?: RateLimit;
    [key: string]: any;
}
